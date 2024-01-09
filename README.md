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
django-admin startproject jobapp_django .
```

### Run Local Server
```sh
python manage.py runserver
python manage.py runserver 8001
```