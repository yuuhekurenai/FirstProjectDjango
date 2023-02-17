from django.urls import path
from . import views

patterns = [
    path('', views.profiles, name='profiles'),
]