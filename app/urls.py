from django.urls import path
# from app.views import hello, job_detail
from app import views

urlpatterns = [
    path('', views.jobs_list, name='jobs_list'),
    path('hello/<str:name>', views.hello, name='hello'),
    path('job/<slug:job_slug>', views.job_detail, name='job_detail')
]
