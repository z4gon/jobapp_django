from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description
    
class FileUpload(models.Model):
    file = models.FileField(upload_to='files')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description