from django.forms import ModelForm
from django import forms
from .models import Project


# O form foi criado com base no modelo Project criado nem Models.py
# A variável fields recebe todos os campos do modelo Project atrás do valor '__all__' ou a lista informada
class Projectform(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_code', 'tags']
        # com widgets é possível modificar diretamente os campos
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

        # criar uma função para modificar os campos também é um opção possível e mais avançada
        def __init__(self, *args, **kwargs):
            super(Projectform, self).__init__(*args, **kwargs)

        #            self.fields['title'].widgets.attrs.update(
        #             {'class': 'input', 'placeholder': 'Add title'})

        #           self.fields['description'].widgets.attrs.update(
        #              {'class': 'input'})

        # Também é possível modificar vários campos utilizando um looping
            for name, field in self.fields.items():
                field.widgets.attrs.update({'class': 'input'})