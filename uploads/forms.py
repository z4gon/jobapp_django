from django import forms
from uploads.models import FileUpload, ImageUpload

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = '__all__'

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'