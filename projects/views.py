from django.shortcuts import render # render recebe a informação passado no settings
#sobre a pasta templates, então agora podemos referencia-la utilizando return render.

from django.http import HttpResponse


def projects(request):
    return render(request, 'projects/project.html')


def project(request, pk):
    return render(request, 'projects/single-project.html')

