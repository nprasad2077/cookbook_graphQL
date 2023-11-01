# Activate Python Shell Environement and install deps

1. pip install pipenv
2. pipenv shell
3. pip install django graphene_django

### Then, create the Django Project and Application

1. django-admin startproject cookbook
2. cd cookbook
3. django-admin startapp ingredients

### Then, Sync Database for the first time

1. python3 manage.py migrate
