from django.contrib import admin
from app.models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'salary', 'description', 'id')
    list_filter = ('company', 'salary')
    search_fields = ('title', 'company', 'salary', 'description')
    search_help_text = ('Use AND, OR, NOT, " " for phrases, - to exclude terms')

admin.site.register(Job, JobAdmin)