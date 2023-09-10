from django.shortcuts import render,get_object_or_404
from .models import Skill, Project

# Create your views here.

def index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'skills/index.html', {'skills': skills, 'projects': projects})

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'skills/project.html', {'project': project})