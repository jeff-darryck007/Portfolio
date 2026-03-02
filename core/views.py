from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.filter(featured=True).order_by('-created_at')[:3]
    skills = Skill.objects.all().order_by('-proficiency')
    return render(request, 'core/index.html', {
        'projects': projects,
        'skills': skills
    })
