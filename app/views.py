from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from app.models import Job

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

def jobs_list(request):
    context = {
        'jobs': Job.objects.all()
    }

    return render(request, 'app/jobs_list.html', context)

def job_detail(request, job_id):
    try:
        if job_id == 0:
            return redirect(reverse('jobs_list')) # redirect home

        context = {
            'job': Job.objects.get(id=job_id), # fails if not found
        }
        
        return render(request, 'app/job_detail.html', context)   
    
    except ObjectDoesNotExist:
        return render(request, 'app/job_not_found.html', {}, status=404)   