from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello World")

def job_detail(request, job_id):
    return HttpResponse(f"Job details for: {job_id = }")