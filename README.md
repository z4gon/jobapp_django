# Jobs Portal Website (Django 4.x)
A Jobs Postings Portal built with Django 4

- [Jobs Portal Website (Django 4.x)](#jobs-portal-website-django-4x)
  - [Resources](#resources)
  - [Local Setup](#local-setup)
    - [Install Django](#install-django)
    - [Activate Virtualenv](#activate-virtualenv)
    - [Create a Project](#create-a-project)
  - [Django Utility Commands](#django-utility-commands)
    - [Run Local Server](#run-local-server)
    - [Create App in Project](#create-app-in-project)
  - [Project Structure](#project-structure)
  - [URLs](#urls)
    - [Path Converters](#path-converters)
    - [Reverse URLs](#reverse-urls)
    - [Redirect](#redirect)
  - [Templates](#templates)

## Resources
[Python Django 4 Masterclass | Build a Real World Project](https://www.udemy.com/course/python-django-masterclass)

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
│  ├─ templates/
│  ├─ ├─ some_template.html
│  ├─ views.py
├─ manage.py
```

## URLs

### Path Converters
Two paths with different primitive type can coexist.

```py
urlpatterns = [
    path('', views.jobs_list),
    path('job/<int:job_id>', views.job_detail)
    path('job/<str:job_id>', views.job_detail)
    path('blog/<slug:blog_slug>', views.post_detail)
    path('product/<uuid:product_id>', views.product_detail)
]
```

### Reverse URLs
```py
urlpatterns = [
    path('', views.jobs_list, name='jobs_list'),
    path('job/<int:job_id>', views.job_detail, name='job_detail')
]
```

```py
url = reverse('job_detail', args=[job_id])
```

### Redirect
```py
def job_detail(request, job_id):
    if job_id not in all_jobs:
        return redirect(reverse('jobs_list')) # redirect home
```

## Templates
Django scans the apps in this order looking for templates by name.
```py
INSTALLED_APPS = [
    ...
    'my_app.apps.AppConfig'
]
```

Namespacing, ensures no conflicts arise from templates with same name.
```sh
my_project/
├─ my_app/
│  ├─ templates/
│  ├─ ├─ my_app/
│  ├─ ├─ ├─ index.html
├─ my_other_app/
│  ├─ templates/
│  ├─ ├─ my_other_app/
│  ├─ ├─ ├─ index.html
│  ├─ views.py
```

```py
template = loader.get_template('hello.html')
context = { ... }
return HttpResponse(template.render(context, request))
```

```py
context = { ... }
return render(request, 'app/hello.html', context)   
```