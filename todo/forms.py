from django.db.models import fields
from .models import Tarefa
from django import forms

class AdicionarTarefa(forms.ModelForm):
     
     class Meta:
         model = Tarefa
         fields = ['tarefa']