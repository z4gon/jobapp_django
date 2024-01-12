from enum import unique
from pyexpat import model
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.street}, {self.state}, {self.city}, {self.country} {self.zip}"
    
class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name}"
    
class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField(default=0)
    slug = models.SlugField(null=True, max_length=200, unique=True)

    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, null=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.title} - {self.company} - ${self.salary}"
    
    # https://docs.djangoproject.com/en/4.2/topics/db/models/#overriding-model-methods
    def save(self, *args, **kwargs):
        if not self.id: # only on creation
            self.slug = slugify(self.title + "-" + self.company)

        return super().save(*args, **kwargs)