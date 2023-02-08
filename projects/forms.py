from django.forms import ModelForm
from .models import Project

# O form foi criado com base no modelo Project criado nem Models.py
# A variável fields recebe todos os campos do modelo Project atrás do valor '__all__'
class Projectform(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
