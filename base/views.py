from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Task

# from django.http import HttpResponse

# Create your views here.
class TaskList(ListView):
    # return HttpResponse('To Do list')
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    context_object_name = 'task'
    fields = '__all__'
    success_url = reverse_lazy('tasks')