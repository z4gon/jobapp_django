from django.shortcuts import render

from uploads.forms import FileUploadForm, ImageUploadForm

# Create your views here.

def upload_image(request):
    form = ImageUploadForm()
    
    if request.POST:
        form = ImageUploadForm(request.POST, request.FILES) # bound
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request, 'uploads/upload_image.html', { "form" : form, "saved_object": saved_object })

    return render(request, 'uploads/upload_image.html', { "form" : form })

def upload_file(request):
    form = FileUploadForm()
    
    if request.POST:
        form = FileUploadForm(request.POST, request.FILES) # bound
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request, 'uploads/upload_file.html', { "form" : form, "saved_object": saved_object })

    return render(request, 'uploads/upload_file.html', { "form" : form })