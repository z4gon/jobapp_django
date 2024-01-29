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
  - [URLs and Views](#urls-and-views)
    - [Path Converters](#path-converters)
    - [Reverse URLs](#reverse-urls)
    - [Redirect](#redirect)
    - [Manual POST \& CSRF](#manual-post--csrf)
  - [Templates](#templates)
    - [Context](#context)
    - [If / Else](#if--else)
    - [For Loops](#for-loops)
    - [Reverse URLs](#reverse-urls-1)
  - [Admin](#admin)
    - [createsuperuser](#createsuperuser)
    - [Register Model](#register-model)
    - [Register Admin Model](#register-admin-model)
    - [List Display](#list-display)
    - [List Filter](#list-filter)
    - [Search Fields](#search-fields)
    - [Search Help](#search-help)
    - [Details Fields](#details-fields)
    - [Fieldsets](#fieldsets)
    - [Admin CSS](#admin-css)
  - [ORM](#orm)
    - [Models, Field Types \& Options](#models-field-types--options)
    - [Migrations](#migrations)
      - [makemigrations](#makemigrations)
        - [Add Fields to a Model](#add-fields-to-a-model)
      - [sqlmigrate](#sqlmigrate)
      - [showmigrations](#showmigrations)
      - [migrate](#migrate)
    - [Data Migrations](#data-migrations)
    - [Insert](#insert)
    - [Select Many](#select-many)
      - [To String](#to-string)
    - [Select Single](#select-single)
    - [Where](#where)
      - [Chain QuerySets](#chain-querysets)
    - [Exclude](#exclude)
    - [Limit](#limit)
    - [Order By](#order-by)
    - [Fields Lookup](#fields-lookup)
    - [Update](#update)
    - [Overriding Model Funcs](#overriding-model-funcs)
      - [save()](#save)
    - [Aggregation](#aggregation)
    - [Delete](#delete)
    - [One To One Relationship](#one-to-one-relationship)
      - [One To One Restriction](#one-to-one-restriction)
      - [One To One Query](#one-to-one-query)
    - [One To Many Relationship](#one-to-many-relationship)
      - [One To Many Assign](#one-to-many-assign)
      - [One To Many Query](#one-to-many-query)
    - [Many To Many Relationship](#many-to-many-relationship)
      - [Many To Many Assign](#many-to-many-assign)
      - [Many To Many Query](#many-to-many-query)
  - [Forms](#forms)
    - [POST](#post)
    - [Rendering](#rendering)
      - [Layout](#layout)
      - [Manual](#manual)
    - [Validation](#validation)
      - [Clean Methods](#clean-methods)
      - [Custom Validators](#custom-validators)
    - [Model Form](#model-form)
      - [Save](#save-1)
      - [Choices](#choices)
  - [Static Files](#static-files)

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

## URLs and Views

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

### Manual POST & CSRF
```py
def subscribe(request):
    context = {}

    if request.POST:
        email = request.POST.get('email')

        errors = []
        if email == "":
            errors.append("Email is required")
        context["errors"] = errors

        if len(errors) == 0:
            # save the subscriber to the database
            subscriber = Subscriber(first_name=first_name, last_name=last_name, email=email)
            subscriber.save()

    return render(request, 'subscriptions/subscribe.html', context)
```

```html
<form method="post">
    <!-- django csrf token -->
    {% csrf_token %}

    <label for="email">Email</label>
    <input type="email" name="email" placeholder="Your Email" required />

    <!-- show errors -->
    {% if errors %}
      {% for error in errors %}
      <p style="color: red">{{ error }}</p>
      {% endfor %}
    {% endif %}

    <input type="submit" value="Submit" />
  </form>
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

### Context
```py
def hello(request, name):
    context = {
        'name': name,
        'age': 25,
        'my_list': ['alpha', 'beta', 'gamma', 'delta'],
        'my_object': AuxClass()
    }
    return render(request, 'app/hello.html', context)  
```

```html
<h1>Hello {{ name }}!</h1>
<h3>Your age is: {{ age }}</h3>
<p>{{ my_list.0 }}</p>
<p>{{ my_list.1 }}</p>
<p>{{ my_list.2 }}</p>
<p>{{ my_list.3 }}</p>
{{ my_object.x }}
```

### If / Else
```html
{% if starts_with_a %}
    <h3>Your name starts with A!</h3>
{% else %}
    <h3>Your name doesn't start with A!</h3>
{% endif %}
```

### For Loops
```html
{% for elem in my_list %}
    <p>{{ elem }}</p>
{% endfor %}
```

### Reverse URLs
```html
<a href={% url "job_detail" job.id %}>
```

## Admin

### createsuperuser

```sh
python manage.py createsuperuser
```

### Register Model

```py
from django.contrib import admin
from app.models import Job

admin.site.register(Job)
```

### Register Admin Model
```py
# app/admin.py

from django.contrib import admin
from app.models import Job

class JobAdmin(admin.ModelAdmin):
    pass

admin.site.register(Job, JobAdmin)
```

### List Display
```py
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary', 'description', 'id')
```
```py
class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')
```

### List Filter
```py
class JobAdmin(admin.ModelAdmin):
    list_filter = ('company', 'salary')
```

### Search Fields
```py
class JobAdmin(admin.ModelAdmin):
    search_fields = ('title', 'company', 'salary', 'description')
```

### Search Help
```py
class JobAdmin(admin.ModelAdmin):
    search_help_text = ('Use AND, OR, NOT, " " for phrases, - to exclude terms')
```

### Details Fields
Fields to display, can group in Touples
```py
class JobAdmin(admin.ModelAdmin):
    fields = (('title', 'company'), 'salary', 'description')
```
Fields to exclude
```py
class JobAdmin(admin.ModelAdmin):
    exclude = ('slug')
```

### Fieldsets
```py
class JobAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'description': 'The minimal information about the Job.',
            'fields': (('title', 'company'), 'salary')
        }),
        ('Extra Information', {
            'fields': ('description',)
        })
    )
```

### Admin CSS
```py
class JobAdmin(admin.ModelAdmin):
    fieldsets = (
        ...
        ('Extra Information', {
            'fields': ('description',)
            'classes': ('collapse',)
        })
    )
```

## ORM

### Models, Field Types & Options

```py
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
```

### Migrations

#### makemigrations

Creates new migrations based on the changes that are identified in the models.
```sh
python manage.py makemigrations
```

```py
# app/migrations/0001_initial.py

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
```
##### Add Fields to a Model
```sh
python manage.py makemigrations
It is impossible to add the field 'date' with 'auto_now_add=True' to job without providing a default. This is because the database needs something to populate existing rows.
 1) Provide a one-off default now which will be set on all existing rows
 2) Quit and manually define a default value in models.py.
Select an option: 1
Please enter the default value as valid Python.
Accept the default 'timezone.now' by pressing 'Enter' or provide another value.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
[default: timezone.now] >>> timezone.now()
Migrations for 'app':
  app/migrations/0002_job_date_job_salary.py
    - Add field date to job
    - Add field salary to job
```

```py
# app/migrations/0002_job_date_job_salary.py

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 1, 11, 17, 57, 40, 428226, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
```

#### sqlmigrate

Displays the SQL statements for a migration.
```sh
python manage.py sqlmigrate app 0001
```
```sql
BEGIN;
--
-- Create model Job
--
CREATE TABLE "app_job" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "company" varchar(200) NOT NULL, "description" text NOT NULL);
COMMIT;
```

#### showmigrations

Lists the migrations of the project along their status.
```sh
python manage.py showmigrations
```
```sh
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
app
 [ ] 0001_initial
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
```

#### migrate

Runs, applies or unapplies migrations.
```sh
python manage.py migrate
```
```sh
Operations to perform:
  Apply all migrations: admin, app, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying app.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

### [Data Migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/#data-migrations)

```sh
python manage.py makemigrations --empty yourappname
```

```py
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_job_slug'),
    ]

    operations = [
    ]
```

### Insert
```sh
python manage.py shell
```
```sh
>>> from app.models import Job
```
```sh
>>> job_post_1 = Job(title="Software Engineer", company="Facebook", description="Contribute to the React Library", salary=100000)
>>> job_post_1.save()
```
```sh
>>> Job.objects.create(title="Software Engineer II", company="Innersloth", description="Work on Among Us", salary=120000)
```

### Select Many
Returns QuerySet
```sh
>>> Job.objects.all()
<QuerySet [<Job: Job object (1)>, <Job: Job object (2)>, <Job: Job object (3)>]>
```

#### To String
```py
class Job(models.Model):
    ...
    
    def __str__(self):
        return f"{self.title} - {self.company}"
```
```sh
>>> Job.objects.all()
<QuerySet [<Job: Software Engineer - Facebook>, <Job: Software Engineer II - Innersloth>, <Job: Software Engineer III - Thatgamecompany>]>
```

### Select Single
Returns an instance of the model
```sh
>>> Job.objects.get(title="Software Engineer II")
<Job: Software Engineer II - Innersloth>
```
Error when none exist:
```sh
>>> Job.objects.get(title="Non existent title")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "~/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "~/django/db/models/query.py", line 637, in get
    raise self.model.DoesNotExist(
app.models.Job.DoesNotExist: Job matching query does not exist.
```
Error when multiple exist:
```sh
>>> Job.objects.get(salary=110000)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "~/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "~/django/db/models/query.py", line 640, in get
    raise self.model.MultipleObjectsReturned(
app.models.Job.MultipleObjectsReturned: get() returned more than one Job -- it returned 2!
```

### Where
```sh
>>> Job.objects.filter(description="Contribute to the React Library")
```

#### Chain QuerySets
```sh
>>> Job.objects.filter().exclude(company="Facebook").filter(title__contains="Engineer")
```

### Exclude
```sh
>>> Job.objects.exclude(company="Riot Games")
```

### [Limit](https://docs.djangoproject.com/en/5.0/topics/db/queries/#limiting-querysets)
[QuerySets are lazy](https://docs.djangoproject.com/en/5.0/topics/db/queries/#querysets-are-lazy) – the act of creating a QuerySet doesn’t involve any database activity. You can stack filters together all day long, and Django won’t actually run the query until the QuerySet is evaluated.

For example, this returns the first 5 objects (LIMIT 5):
```sh
>>> Entry.objects.all()[:5]
```
For example, this returns the first 5 objects (OFFSET 5 LIMIT 5):
```sh
>>> Entry.objects.all()[5:10]
```

### Order By
```sh
>>> Job.objects.order_by("company")
```
```sh
>>> Job.objects.order_by("-company")
```
```sh
>>> Job.objects.order_by("company", "description")
```

### Fields Lookup
```sh
>>> Job.objects.filter(salary__gt=100000)
```
```sh
>>> Job.objects.filter(LessThan(F("salary"), 120000))
```

### Update
```sh
>>> job_post_1 = Job.objects.filter()[0]
>>> job_post_1.salary
100000
>>> job_post_1.salary = 150000
>>> job_post_1.salary
150000
>>> job_post_1.save()
```

### Overriding Model Funcs

#### save()

```py
class Job(models.Model):
    ...
    slug = models.SlugField(null=True, max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + "-" + self.company)
        return super.save(*args, **kwargs)
```
```sh
>>> Job.objects.create(title="Technical Artist", company="Blizzard", description="Improve content creation pipelines", salary=130000)
```
```sh
job_post_1 = Job.objects.get(id=5)
job_post_1.slug
'technical-artist-blizzard'
```

### Aggregation
```sh
>>> Job.objects.count()
5
```
```sh
>>> from django.db.models import Avg
>>> Job.objects.aggregate(Avg("salary"))
{'salary__avg': 125000.0}
```
```sh
>>> Job.objects.filter()[:3].aggregate(Avg("salary"))
{'salary__avg': 128333.33333333333}
```
```sh
>>> Job.objects.filter(company__icontains="game").count()
2
```
```sh
>>> Job.objects.aggregate(Max("salary"))
{'salary__max': 150000}
```
```sh
>>> Job.objects.aggregate(max_deviation_from_avg=Max("salary") - Avg("salary"))
{'max_deviation_from_avg': 25000.0}
```

### Delete
```sh
>>> my_job = Job.objects.get(id=6)
>>> my_job.delete()
(1, {'app.Job': 1})
```
```sh
>>> all_jobs = Job.objects.all()
>>> all_jobs.delete()
```

### One To One Relationship
```py
# app/models.py

class Location(models.Model):
    ...
    
class Job(models.Model):
    ...

    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
```
Migrations
```sh
python manage.py makemigrations
```
```sh
Migrations for 'app':
  app/migrations/0005_location_job_location.py
    - Create model Location
    - Add field location to job
```
```py
# app/migrations/0005_location_job_location.py

migrations.AddField(
    model_name='job',
    name='location',
    field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.location'),
),
```
```sh
python manage.py sqlmigrate app 0005_location_job_location
```
```sql
BEGIN;
--
-- Create model Location
--
CREATE TABLE "app_location" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "street" varchar(200) NOT NULL, 
  "city" varchar(200) NOT NULL, 
  "state" varchar(200) NOT NULL, 
  "country" varchar(200) NOT NULL, 
  "zip" varchar(200) NOT NULL
);
--
-- Add field location to job
--
CREATE TABLE "new__app_job" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "title" varchar(200) NOT NULL, 
  "company" varchar(200) NOT NULL, 
  "description" text NOT NULL, 
  "date" datetime NOT NULL, 
  "salary" integer NOT NULL, 
  "slug" varchar(200) NULL UNIQUE, 
  "location_id" bigint NULL UNIQUE REFERENCES "app_location" ("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "new__app_job" (
  "id", 
  "title", 
  "company", 
  "description", 
  "date", 
  "salary", 
  "slug", 
  "location_id"
) SELECT 
  "id", 
  "title", 
  "company", 
  "description", 
  "date", 
  "salary", 
  "slug", 
  NULL 
FROM "app_job";

DROP TABLE "app_job";
ALTER TABLE "new__app_job" RENAME TO "app_job";

COMMIT;
```
```sh
python manage.py migrate
```
```sh
Operations to perform:
  Apply all migrations: admin, app, auth, contenttypes, sessions
Running migrations:
  Applying app.0005_location_job_location... OK
```

#### One To One Restriction

```sh
>>> from app.models import Job, Location
>>> l1 = Location(street="Hacker Street", city="Microchips", state="Motherboard", country="PC", zip="12345")
>>> l1.save()
>>> job1 = Job.objects.get(id=1)
>>> job1.location = l1
>>> job1.save()
>>> job2 = Job.objects.get(id=2)
>>> job2.location = l1
>>> job2.save()
...
django.db.utils.IntegrityError: UNIQUE constraint failed: app_job.location_id
```

#### One To One Query
Direct
```sh
>>> job_oxenfurt = Job.objects.filter(location__city="Oxenfurt")
```
Reverse
```sh
>>> location_keen = Location.objects.filter(job__company__icontains="keen")
```

### One To Many Relationship
```py
# app/models.py

class Author(models.Model):
    ...
    
class Job(models.Model):
    ...

    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=False)
```
Migrations
```sh
python manage.py makemigrations
```
```sh
Migrations for 'app':
  app/migrations/0006_author_job_author.py
    - Create model Author
    - Add field author to job
```
```py
# app/migrations/0006_author_job_author.py

migrations.AddField(
    model_name='job',
    name='author',
    field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.author'),
),
```
```sh
python manage.py sqlmigrate app 0005_location_job_location
```
```sql
BEGIN;
--
-- Create model Author
--
CREATE TABLE "app_author" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "name" varchar(200) NOT NULL, 
  "email" varchar(200) NOT NULL
);
--
-- Add field author to job
--
ALTER TABLE "app_job" 
ADD COLUMN "author_id" bigint NULL REFERENCES "app_author" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "app_job_author_id_9e07b364" ON "app_job" ("author_id");

COMMIT;
```
```sh
python manage.py migrate
```
```sh
Operations to perform:
  Apply all migrations: admin, app, auth, contenttypes, sessions
Running migrations:
  Applying app.0006_author_job_author... OK
```

#### One To Many Assign
```sh
>>> from app.models import Location, Author, Job
>>> a1 = Author.objects.get(id=1)
>>> j2 = Job.objects.get(id=2)
>>> j2.author = a1
>>> j2.save()
```

#### One To Many Query
Direct
```sh
>>> Job.objects.filter(author__name__icontains="Geralt")
```
```sh
>>> Job.objects.filter(author__in=[2])
```
```sh
>>> Job.objects.filter(author__pk=2)
```
```sh
>>> Job.objects.filter(author=a1)
```

Reverse
```sh
>>> Author.objects.get(id=1).job_set.all()
```
```sh
>>> Author.objects.get(id=1).job_set.count()
```
```sh
>>> Author.objects.get(id=1).job_set.filter(title__icontains="eng")
```
```sh
>>> Author.objects.filter(job__id=1)
```
```sh
>>> Author.objects.filter(job__pk=1)
```
```sh
>>> Author.objects.filter(job__title__icontains="eng")
```
```sh
>>> Author.objects.filter(job=j2)
```

Insert
```sh
>>> Author.objects.get(id=1).job_set.create(...)
```
```sh
>>> a1.jobs_set.add(j1)
```

### Many To Many Relationship
```py
# app/models.py

class Skill(models.Model):
    ...
    
class Job(models.Model):
    ...

    skills = models.ManyToManyField(Skill)
```
Migrations
```sh
python manage.py makemigrations
```
```sh
Migrations for 'app':
  app/migrations/0007_skill_job_skills.py
    - Create model Skill
    - Add field skills to job
```
```py
# app/migrations/0007_skill_job_skills.py

migrations.AddField(
    model_name='job',
    name='skills',
    field=models.ManyToManyField(to='app.skill'),
),
```
```sh
python manage.py sqlmigrate app 0007_skill_job_skills
```
```sql
BEGIN;
--
-- Create model Skill
--
CREATE TABLE "app_skill" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "name" varchar(200) NOT NULL UNIQUE
);
--
-- Add field skills to job
--
CREATE TABLE "app_job_skills" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "job_id" bigint NOT NULL REFERENCES "app_job" ("id") DEFERRABLE INITIALLY DEFERRED, 
  "skill_id" bigint NOT NULL REFERENCES "app_skill" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE UNIQUE INDEX "app_job_skills_job_id_skill_id_1fb03c4b_uniq" ON "app_job_skills" ("job_id", "skill_id");
CREATE INDEX "app_job_skills_job_id_6d88a2c2" ON "app_job_skills" ("job_id");
CREATE INDEX "app_job_skills_skill_id_3de09170" ON "app_job_skills" ("skill_id");

COMMIT;
```
```sh
python manage.py migrate
```
```sh
Operations to perform:
  Apply all migrations: admin, app, auth, contenttypes, sessions
Running migrations:
  Applying app.0007_skill_job_skills... OK
```

#### Many To Many Assign
```sh
>>> from app.models import Job, Skill
>>> s1 = Skill.objects.get(name="React")
>>> j1 = Job.objects.get(id=1)
>>> j1.skills.add(s1)
```
```sh
>>> s4 = Skill.objects.get(name="Shaders")
>>> j5 = Job.objects.get(id=5)
>>> s4.job_set.add(j5)
```

#### Many To Many Query
Direct
```sh
>>> j1.skills.all()
```
```sh
>>> Job.objects.filter(skills__name__icontains="Shader")
```
```sh
>>> Job.objects.filter(skills__name__startswith=="s")
```
```sh
>>> Job.objects.filter(skills=s4)
```
```sh
>>> Job.objects.filter(skills__in=[1,2])
>>> Job.objects.filter(skills__in=[1,2]).distinct()
```

Reverse
```sh
>>> s4.job_set.all()
```
```sh
>>> Skill.objects.filter(job__title__icontains="eng")
```

Remove
```sh
>>> j5.skills.remove(s4)
```
```sh
>>> j1.skills.clear()
```

Insert
```sh
>>> j1.skills.set([s1, s2])
```
```sh
>>> s3.job_set.add(j1, j2)
```

## Forms

### POST
```py
# forms.py

class SubscriberForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
```
```html
<!-- subscribe.html -->

<form method="post">
  <!-- django csrf token -->
  {% csrf_token %} {{ form }}
  <input type="submit" value="Submit" />
</form>
```
```py
# views.py

def subscribe(request):
    subscribe_form = SubscriberForm()

    if request.POST:
        subscribe_form = SubscriberForm(request.POST) # bound

        if subscribe_form.is_valid():
            print(f"VALID FORM {subscribe_form.first_name = } {subscribe_form.last_name = } {subscribe_form.email = }")

            #     # save the subscriber to the database
            #     subscriber = Subscriber(first_name=first_name, last_name=last_name, email=email)
            #     subscriber.save()

    context = { "form" : subscribe_form }
    return render(request, 'subscriptions/subscribe.html', context)
```

### Rendering

#### Layout
1. `as_p`
2. `as_table`
3. `as_ul`
   
#### Manual
```html
<!-- subscribe.html -->

<form method="post">
  {{ form.first_name.errors }}
  <label for="{{ form.first_name.id_for_label }}">{{ form.first_name.label }}</label>
  {{ form.first_name }}
  {{ form.help_text }}
</form>
```
```html
<!-- subscribe.html -->

<form method="post">
  {% for field in form %}
  <div class="my_field">
    {{ field.errors }}
    <!-- {{ field.label_tag }} -->
    <label for="{{ field.id_for_label }}">{{ field.label }}</label>
    {{ field }}
  </div>
  {% endfor %}
</form>
```
   
### Validation

#### Clean Methods

```py
class SubscriberForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, help_text="Enter characters only")

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if ',' in data:
            raise forms.ValidationError("Invalid First Name, please enter characters only")
```

#### Custom Validators

```py
def validate_no_comma(value):
    if ',' in value:
        raise forms.ValidationError("This value cannot include a comma")

class SubscriberForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, help_text="Enter characters only", validators=[validate_no_comma])
```

### Model Form
```py
class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = "__all__"
        # fields = ['first_name', 'last_name', 'email']
```

#### Save
```py
def subscribe(request):
    subscribe_form = SubscriberForm()

    if request.POST:
        subscribe_form = SubscriberForm(request.POST) # bound

        if subscribe_form.is_valid():
            subscribe_form.save()
```

#### Choices
```py
NEWSLETTER_OPTION = [
    ('W', 'Weekly'),
    ('M', 'Monthly'),
    ('N', 'Never')
]

# subscriber model
class Subscriber(models.Model):
    option = models.CharField(max_length=1, choices=NEWSLETTER_OPTION, default='W')
```

## Static Files

Namespacing, ensures no conflicts arise from files with same name.
```sh
my_project/
├─ my_project/
├─ my_app/
│  ├─ static/
│  ├─ ├─ my_app/
│  ├─ ├─ ├─ main.css
```

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
	<head>
		<link href="{% static 'main.css' %}" rel="stylesheet" type="text/css" />
	</head>
</html>
```