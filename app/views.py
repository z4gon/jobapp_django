from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h3>Hello, World!</h3>")

def job_detail(request, job_id):
    url = f"https://www.linkedin.com/jobs/view/{job_id}"
    return HttpResponse(f"""
        <h1>Job details for: {job_id}</h1>
        Visit <a href={url}>this link</a> for more info.
    """)