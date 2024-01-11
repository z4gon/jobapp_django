from django.db import models
from django.db.models.functions import Now

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.company} - {self.salary}"
    