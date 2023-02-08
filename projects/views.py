from django.shortcuts import render
from .models import Project
# render recebe a informação passado no settings
# sobre a pasta templates, então agora podemos referenciá-la utilizando return render.

from django.http import HttpResponse

ProjectList = [
    {
        'id': '1',
        'title': "Ecommerce Website",
        'description': 'Fully functional ecommerce website',
    },
    {
        'id': '2',
        'title': "Portfolio Website",
        'description': 'This was a project where I built out my portifolio',
    },
    {
        'id': '3',
        'title': "Social Network",
        'description': ' Awesome open source project I am still working on'
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    ProjectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': ProjectObj})
