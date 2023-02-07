from django.contrib import admin
from .models import Project, Review, Tag

# Aqui é possível adicionar e atualizar os modelos do Admin Panel.
# Não esquecer de colocar admin.site para registrar o novo modelo.

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)