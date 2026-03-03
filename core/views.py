from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project, Skill, Experience, Category, Testimonial, CompanySetting, Post, ContactMessage


def home(request):
    projects = Project.objects.filter(featured=True).order_by('-created')[:3]
    skills = Skill.objects.all().order_by('-proficiency')
    return render(request, 'core/index.html', {
        'projects': projects,
        'skills': skills
    })

def about(request):
    return render(request, 'about.html')

def experience(request):
    return render(request, 'experience.html')

def blog(request):
    return render(request, 'feed.html')

def blog_detail(request, pk=None):
    return render(request, 'blog_detail.html')

def contact(request):
    return render(request, 'contact.html')

def project_list(request):
    return render(request, 'project.html')

def cv(request):
    return render(request, 'cv.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Admin CRUD Views
class AdminProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'admin/project_list.html'
    context_object_name = 'projects'

class AdminExperienceListView(LoginRequiredMixin, ListView):
    model = Experience
    template_name = 'admin/experience_list.html'
    context_object_name = 'experiences'

class AdminSkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'admin/skill_list.html'
    context_object_name = 'skills'

class AdminCategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'admin/category_list.html'
    context_object_name = 'categories'

class AdminPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'admin/post_list.html'
    context_object_name = 'posts'

class AdminTestimonialListView(LoginRequiredMixin, ListView):
    model = Testimonial
    template_name = 'admin/testimonial_list.html'
    context_object_name = 'testimonials'

class AdminContactMessageListView(LoginRequiredMixin, ListView):
    model = ContactMessage
    template_name = 'admin/contact_list.html'
    context_object_name = 'messages'

class AdminCompanySettingListView(LoginRequiredMixin, ListView):
    model = CompanySetting
    template_name = 'admin/settings_list.html'
    context_object_name = 'settings'
