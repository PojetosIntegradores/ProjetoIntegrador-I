from django.db import models

# Create your models here.
class Tarefa(models.Model):
    tarefa = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tarefa