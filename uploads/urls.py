from django.urls import path
from uploads import views

urlpatterns = [
    path('upload_image', views.upload_image, name='upload_image'),
]
