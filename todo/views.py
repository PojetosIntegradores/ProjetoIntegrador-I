from django.shortcuts import redirect, render
from .models import Tarefa
from .forms import *

tarefas = ['aprender django', 'estudar selenium', 'classes online']

def home(request):
    tarefas = Tarefa.objects.all()
    context = { 'tarefas': tarefas }
    return render(request, 'todo/home.html', context)

def add(request):
    if request.method == 'POST':
        form = AdicionarTarefa(request.POST)
        if form.is_valid():
            # tarefa = form.cleaned_data["tarefa"]
            # print(tarefa)
            form.save()
            return redirect("home")
    else:
        form = AdicionarTarefa()
    context = {'form': form}
    return render(request, 'todo/add.html', context)

def deletar(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    return redirect("home")

def editar(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    if request.method == 'POST':
        form = AdicionarTarefa(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AdicionarTarefa(instance=tarefa)
    context = {'form': form}
    return render(request, 'todo/editar.html', context)