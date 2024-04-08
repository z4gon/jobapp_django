from django.contrib import admin
from uploads.models import FileUpload, ImageUpload

# Register your models here.

admin.site.register(ImageUpload)
admin.site.register(FileUpload)