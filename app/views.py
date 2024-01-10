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

def jobs_list(request):
    jobs_html = [
        f"""
        <li>
            <h2>{job.get("title")}</h1>
            <h3>{job.get("company")}</h2>
            <p>{job.get("location")}</p>
            Visit <a href=/job/{job.get("id")}>this link</a> for more info.
        </li>
        """ for job in all_jobs.values()
    ]

    return HttpResponse(f"""
        <h1>Jobs List</h1>
        <hr />
        <ul>
            {"".join(jobs_html)}
        </ul>
    """)

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