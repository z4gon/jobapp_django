# Jobs Portal Website (Django 4.x)
A Jobs Postings Portal built with Django 4

## Local Setup
- pyenv
- pipenv

### Activate Virtualenv
```sh
source $(pipenv --venv)/bin/activate
```

Then you will be able to do:
```
django-admin --version
4.2.9
```

### Create a Project with Django Admin
```sh
django-admin startproject my_project .
```

## manage.py

### Run Local Server
```sh
python manage.py runserver
python manage.py runserver 8001
```

### Create App in Project
```sh
python manage.py startapp my_app
```