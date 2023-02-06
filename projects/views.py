from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def projects(request):
    return HttpResponse('Aqui está o primeiro projeto')


def project(request, pk):
    return HttpResponse('Aqui está o primeiro projeto unico' + ' ' + str(pk))

