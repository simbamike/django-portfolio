from django.shortcuts import render
from portfolio.models import Project

# Create your views here.

def index(request):
    """The homepage for the Portfolio"""
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/index.html', context)

def project(request, pid):
    """Display the details of the proj"""
    project = Project.objects.get(id = pid)
    context = {
        'project': project
    }
    return render (request, 'portfolio/project.html', context)
