from django.db import models
from django.utils.text import slugify

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField(default=0)
    slug = models.SlugField(null=True, max_length=200, unique=True)

    def __str__(self):
        return f"{self.title} - {self.company} - ${self.salary}"
    
    # https://docs.djangoproject.com/en/4.2/topics/db/models/#overriding-model-methods
    def save(self, *args, **kwargs):
        if not self.id: # only on creation
            self.slug = slugify(self.title + "-" + self.company)

        return super().save(*args, **kwargs)