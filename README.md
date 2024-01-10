# Jobs Portal Website (Django 4.x)
A Jobs Postings Portal built with Django 4

- [Jobs Portal Website (Django 4.x)](#jobs-portal-website-django-4x)
  - [Local Setup](#local-setup)
    - [Install Django](#install-django)
    - [Activate Virtualenv](#activate-virtualenv)
    - [Create a Project with Django Admin](#create-a-project-with-django-admin)
  - [Django Utility Commands](#django-utility-commands)
    - [Run Local Server](#run-local-server)
    - [Create App in Project](#create-app-in-project)

## Local Setup
- [pyenv](https://github.com/pyenv/pyenv)
- [pipenv](https://pipenv.pypa.io/en/latest/)

### Install Django
```sh
pipenv install django==4.2.9
```

### Activate Virtualenv
```sh
source $(pipenv --venv)/bin/activate
```

Then you will be able to do:
```
django-admin --version
4.2.9
```

### Create a Project
```sh
django-admin startproject my_project .
```

## Django Utility Commands

### Run Local Server
```sh
python manage.py runserver
python manage.py runserver 8001
```

### Create App in Project
```sh
python manage.py startapp my_app
```

## Project Structure
```sh
my_project/
├─ my_project/
│  ├─ asgi.py
│  ├─ wsgi.py
│  ├─ settings.py
│  ├─ urls.py
├─ my_app/
│  ├─ migrations/
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ views.py
├─ manage.py
```
