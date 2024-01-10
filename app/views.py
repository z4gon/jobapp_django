from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader

# Create your views here.

class AuxClass:
    x = 5

def hello(request, name):
    # template = loader.get_template('app/hello.html')
    context = {
        'name': name,
        'age': 25,
        'my_list': ['alpha', 'beta', 'gamma', 'delta'],
        'my_object': AuxClass(),
        'starts_with_a': name.startswith('a')
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'app/hello.html', context)   

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
    context = {
        'jobs': all_jobs.values()
    }

    return render(request, 'app/jobs_list.html', context)

def job_detail(request, job_id):
    try:
        if job_id == 0:
            return redirect(reverse('jobs_list')) # redirect home

        context = {
            'job': all_jobs[job_id], # fails if not found
        }
        
        return render(request, 'app/job_detail.html', context)   
    
    except KeyError:
        return render(request, 'app/job_not_found.html', {})   