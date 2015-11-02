# coding:utf8
from django.shortcuts import render
from .models import Project
from django.http import Http404
# Create your views here.

def index(request):
    project_list = Project.objects.order_by('-sign_date')[:5]
    context ={'project_list':project_list, }
    return render(request, 'OA/index.html', context)

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    content = {'project': project}
    return render(request, 'OA/detail.html', content)



