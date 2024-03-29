from django.shortcuts import render

from uploads.forms import ImageUploadForm

# Create your views here.
def upload_image(request):
    form = ImageUploadForm()

    if request.POST:
        form = ImageUploadForm(request.POST, request.FILES) # bound
        if form.is_valid():
            form.save()

    context = { "form" : form }
    return render(request, 'uploads/upload_image.html', context)