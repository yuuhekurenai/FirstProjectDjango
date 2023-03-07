from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
# render recebe a informação passado no settings
# sobre a pasta templates, então agora podemos referenciá-la utilizando return render.

from .forms import Projectform

from django.http import HttpResponse


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    ProjectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': ProjectObj})

@login_required(login_url='login')
def createProject(request):
    form = Projectform()

    if request.method == 'POST':
        form = Projectform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = Projectform(instance=project)

    if request.method == 'POST':
        form = Projectform(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
