from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
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

class AdminCRUDContextMixin:
    model_name = ""
    model_name_plural = ""
    list_url_name = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model_name
        context['model_name_plural'] = self.model_name_plural
        context['list_url_name'] = self.list_url_name
        return context

# Projects
class AdminProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'admin/project_list.html'
    context_object_name = 'projects'

class AdminProjectCreateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, CreateView):
    model = Project
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_projects')
    success_message = "Projet créé avec succès !"
    model_name = "Projet"
    model_name_plural = "Projets"
    list_url_name = "admin_projects"

class AdminProjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, UpdateView):
    model = Project
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_projects')
    success_message = "Projet mis à jour avec succès !"
    model_name = "Projet"
    model_name_plural = "Projets"
    list_url_name = "admin_projects"

class AdminProjectDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_projects')
    success_message = "Projet supprimé avec succès !"

# Experiences
class AdminExperienceListView(LoginRequiredMixin, ListView):
    model = Experience
    template_name = 'admin/experience_list.html'
    context_object_name = 'experiences'

class AdminExperienceCreateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, CreateView):
    model = Experience
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_experiences')
    success_message = "Expérience ajoutée avec succès !"
    model_name = "Expérience"
    model_name_plural = "Expériences"
    list_url_name = "admin_experiences"

class AdminExperienceUpdateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, UpdateView):
    model = Experience
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_experiences')
    success_message = "Expérience mise à jour avec succès !"
    model_name = "Expérience"
    model_name_plural = "Expériences"
    list_url_name = "admin_experiences"

class AdminExperienceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Experience
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_experiences')
    success_message = "Expérience supprimée avec succès !"

# Skills
class AdminSkillListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = 'admin/skill_list.html'
    context_object_name = 'skills'

class AdminSkillCreateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, CreateView):
    model = Skill
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_skills')
    success_message = "Compétence ajoutée avec succès !"
    model_name = "Compétence"
    model_name_plural = "Compétences"
    list_url_name = "admin_skills"

class AdminSkillUpdateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, UpdateView):
    model = Skill
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_skills')
    success_message = "Compétence mise à jour avec succès !"
    model_name = "Compétence"
    model_name_plural = "Compétences"
    list_url_name = "admin_skills"

class AdminSkillDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Skill
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_skills')
    success_message = "Compétence supprimée avec succès !"

# Categories
class AdminCategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'admin/category_list.html'
    context_object_name = 'categories'

class AdminCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, CreateView):
    model = Category
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_categories')
    success_message = "Catégorie créée avec succès !"
    model_name = "Catégorie"
    model_name_plural = "Catégories"
    list_url_name = "admin_categories"

class AdminCategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, UpdateView):
    model = Category
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_categories')
    success_message = "Catégorie mise à jour avec succès !"
    model_name = "Catégorie"
    model_name_plural = "Catégories"
    list_url_name = "admin_categories"

class AdminCategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_categories')
    success_message = "Catégorie supprimée avec succès !"

# Posts
class AdminPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'admin/post_list.html'
    context_object_name = 'posts'

class AdminPostCreateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, CreateView):
    model = Post
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_posts')
    success_message = "Article créé avec succès !"
    model_name = "Article"
    model_name_plural = "Articles"
    list_url_name = "admin_posts"

class AdminPostUpdateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, UpdateView):
    model = Post
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_posts')
    success_message = "Article mis à jour avec succès !"
    model_name = "Article"
    model_name_plural = "Articles"
    list_url_name = "admin_posts"

class AdminPostDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_posts')
    success_message = "Article supprimé avec succès !"

# Testimonials
class AdminTestimonialListView(LoginRequiredMixin, ListView):
    model = Testimonial
    template_name = 'admin/testimonial_list.html'
    context_object_name = 'testimonials'

class AdminTestimonialCreateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, CreateView):
    model = Testimonial
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_testimonials')
    success_message = "Témoignage ajouté avec succès !"
    model_name = "Témoignage"
    model_name_plural = "Témoignages"
    list_url_name = "admin_testimonials"

class AdminTestimonialUpdateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, UpdateView):
    model = Testimonial
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_testimonials')
    success_message = "Témoignage mis à jour avec succès !"
    model_name = "Témoignage"
    model_name_plural = "Témoignages"
    list_url_name = "admin_testimonials"

class AdminTestimonialDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Testimonial
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_testimonials')
    success_message = "Témoignage supprimé avec succès !"

# Contact Messages
class AdminContactMessageListView(LoginRequiredMixin, ListView):
    model = ContactMessage
    template_name = 'admin/contact_list.html'
    context_object_name = 'messages'

class AdminContactMessageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ContactMessage
    template_name = 'admin/confirm_delete.html'
    success_url = reverse_lazy('admin_contact_messages')
    success_message = "Message supprimé avec succès !"

# Company Settings
class AdminCompanySettingListView(LoginRequiredMixin, ListView):
    model = CompanySetting
    template_name = 'admin/settings_list.html'
    context_object_name = 'settings'

class AdminCompanySettingUpdateView(LoginRequiredMixin, SuccessMessageMixin, AdminCRUDContextMixin, UpdateView):
    model = CompanySetting
    template_name = 'admin/model_form.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_settings')
    success_message = "Configuration mise à jour avec succès !"
    model_name = "Configuration"
    model_name_plural = "Configuration"
    list_url_name = "admin_settings"
