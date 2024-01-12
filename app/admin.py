from django.contrib import admin
from app.models import Author, Job, Location, Skill

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    # list
    list_display = ('title', 'salary', 'company', 'location', 'author', 'id')
    list_filter = ('company', 'salary', 'author')
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
            'fields': ('description', 'location', 'author',),
            # 'classes': ('collapse',)
        })
    )

class LocationAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'country', 'zip', 'id')
    list_filter = ('city', 'state', 'country')
    search_fields = ('street', 'city', 'state', 'country', 'zip')
    search_help_text = ('Use AND, OR, NOT, " " for phrases, - to exclude terms')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'id')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')
    search_help_text = ('Use AND, OR, NOT, " " for phrases, - to exclude terms')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    search_help_text = ('Use AND, OR, NOT, " " for phrases, - to exclude terms')

admin.site.register(Job, JobAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Skill, SkillAdmin)
