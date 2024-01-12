from django.contrib import admin
from app.models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary', 'description', 'id')

admin.site.register(Job, JobAdmin)