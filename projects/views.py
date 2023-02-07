from django.shortcuts import render
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
    page = 'Project'
    number = 8
    context = {'page': page, 'number': number, 'projects': ProjectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    ProjectObj = None
    for i in ProjectList:
        if i['id'] == pk:
            ProjectObj = i
    return render(request, 'projects/single-project.html', {'project': ProjectObj})
