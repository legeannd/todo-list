from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from .models import *

class Index(TemplateView):
    template_name = 'index.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['name', 'details', 'timeFinish']
    template_name = 'create.html'

class OwnerCreate(CreateView):
    model = Owner
    fields = ['task', 'username']

class TaskListView(ListView):
    model = Task