from django.urls import path
# from app.views import hello, job_detail
from app import views

urlpatterns = [
    path('', views.home),
    path('job/<int:job_id>', views.job_detail)
]
