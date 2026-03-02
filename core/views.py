from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.filter(featured=True).order_by('-created_at')[:3]
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

def dashboard(request):
    return render(request, 'dashboard.html')
