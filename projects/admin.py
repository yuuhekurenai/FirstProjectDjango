from django.contrib import admin
from .models import Project

# Aqui é possível adicionar e atualizar os modelos do Admin Panel.
admin.site.register(Project) # Não esquecer de colocar admin.site para registrar o novo modelo.
