# ProjetoIntegrador-I
Desafio Criar um site web com framework web,  controle de versão e banco de dados.

Base do projeto segue link:

https://drive.google.com/file/d/1GHvHXKmGciiplebmAhUk1HVyZ3ddXPVK/view?usp=sharing

## No linux: Intalção do virtualenv

desktop:~$ pip3 install virtualenv

## Criando maquina virtual na pasta do seu projeto

desktop:~/suaPasta$ virtualenv env

## Passo 1 ativar venv

desktop:~/suaPasta$ source env/bin/activate

## Virtualenv ativado

(env) desktop:~/suaPasta$

Aqui você pode instalar libs e frameworks de forma isolada e sem medo a env vai funcionar como repositorio de dependencias.

## Criar projeto.
    - pip install django
    - django-admin startproject NomeDoSeuProjeto .

## Criar componete do projeto.
    - python manage.py startapp NomeDoSeuComponete


## Habilita banco de dados
    - python manage.py makemigrations
    - python manage.py migrations
    - python manage.py migrate

## Criar usuario admin
    - python manage.py createsuperuser

## Rodar o sistema
    - python manage.py runserver


## 
    - python manage.py shell