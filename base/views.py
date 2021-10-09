from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Task

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
class CustomLoginView(LoginView): # Essa é a funcionalidade de login customizada do django
    template_name = 'base/login.html'
    fields = '__all__' # Aqui fica as chaves do seu ojeto definida em seus campos de input do django admin
    redirect_authenticated_user = True # Se a operação ocorrer com sucesso o usuario sera autenticado e redireciona a pagina principal
    
    def get_success_url(self):
        return reverse_lazy('tasks') # Aqui fica o redirecionamento após excução com sucesso

class RagisterPage(FormView): # Essa é a funcionalidade de cadastro de usario customizada do django
    template_name = 'base/register.html' # Aqui você pode dar nome ao seu template
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form): # Aqui é identificado se o usuario foi criado com sucesso
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RagisterPage, self).form_valid(form)

    def get(self, *args, **kwargs): # Aqui identifica se o usuario registrado esta autenticado
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RagisterPage, self).get(*args, **kwargs)
    
class TaskList(LoginRequiredMixin, ListView): # Esse é o get/read para listar os itens
    # return HttpResponse('To Do list')
    model = Task # Aqui é definido o modelo que você cria no models.py
    context_object_name = 'tasks' # Aqui você pode dar nome ao objeto que vai usar no seu html

    def get_context_data(self, **kwargs): # Aqui fica o filtro dos dados do banco permitindo que cada usuario só veja o que ele mesmo inseriu no banco
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or '' # Aqui fica a funcionalidade de busca
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context
class TaskDetail(LoginRequiredMixin, DetailView): # Esse é o get/read com id para pegar um unico item
    model = Task
    context_object_name = 'task' 
    template_name = 'base/task.html' 

class TaskCreate(LoginRequiredMixin, CreateView): # Esse é o post/create para inserir novos itens
    model = Task
    context_object_name = 'task'
    fields = ['title', 'description', 'complete'] # Aqui fica as chaves do seu ojeto definida em seus campos de input
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView): # Esse é o put/update para atualizar um item
    model = Task
    context_object_name = 'task'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView): # Esse é o delete para deletar um item
    model = Task
    context_object_name = 'task'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')