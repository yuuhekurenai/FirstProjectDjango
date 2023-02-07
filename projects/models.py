from django.db import models
import uuid


# import da library uuid como garantia de que o id não seja repetido.


# A modelagem do banco de dados utilizando models do Django.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, blank=True)
    source_code = models.CharField(max_length=2000, null=True, blank=True)
    # Criada relação ManyToMany com o modelo Tag, referênciada em aspas simples.
    # A intermediação entre as tabelas é feita automaticamente pelo Django.
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # Set automático da data atual
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False) # Set automatico do ID

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),  # Cria uma lista para selecionar o voto.
    )

    # owner
    # Relaciona as tabelas com a ForeignKey - CASCADE para deletar tudo quando apagado.
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)  # define a dropDownList
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
