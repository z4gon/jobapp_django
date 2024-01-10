from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

all_jobs = {
    1: {
        "id": 1,
        "title": "Python Developer",
        "company": "Google",
        "location": "Mountain View, CA"
    },
    2: {
        "id": 2,
        "title": "Java Developer",
        "company": "Facebook",
        "location": "Menlo Park, CA"
    },
    3: {
        "id": 3,
        "title": "Ruby Developer",
        "company": "Amazon",
        "location": "Seattle, WA"
    }
}

def hello(request):
    return HttpResponse("<h3>Hello, World!</h3>")

def job_detail(request, job_id):
    if job_id not in all_jobs:
        return redirect('/') # redirect home

    job = all_jobs.get(job_id)
    url = f"/job/{job_id}"
    
    return HttpResponse(f"""
        <h1>{job.get("title")}</h1>
        <h2>{job.get("company")}</h2>
        <p>{job.get("location")}</p>
        Visit <a href={url}>this link</a> for more info.
    """)