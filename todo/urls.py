from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('add', views.add, name='add'),
    path("deletar/<int:tarefa_id>/", views.deletar, name='deletar'),
    path("editar/<int:tarefa_id>/", views.editar, name='editar'),
]