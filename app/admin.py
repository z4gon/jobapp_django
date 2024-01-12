from django.contrib import admin
from app.models import Job, Location

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    # list
    list_display = ('title', 'company', 'salary', 'description', 'id')
    list_filter = ('company', 'salary')
    search_fields = ('title', 'company', 'salary', 'description')
    search_help_text = ('Use AND, OR, NOT, " " for phrases, - to exclude terms')

    # detail
    # fields = (('title', 'company'), 'salary', 'description')
    # exclude = ('slug',)
    fieldsets = (
        ('Basic Information', {
            'description': 'The minimal information about the Job.',
            'fields': (('title', 'company'), 'salary')
        }),
        ('Extra Information', {
            'fields': ('description', 'location',),
            # 'classes': ('collapse',)
        })
    )

class LocationAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'country', 'zip', 'id')
    list_filter = ('city', 'state', 'country')
    search_fields = ('street', 'city', 'state', 'country', 'zip')
    search_help_text = ('Use AND, OR, NOT, " " for phrases, - to exclude terms')

admin.site.register(Job, JobAdmin)
admin.site.register(Location, LocationAdmin)