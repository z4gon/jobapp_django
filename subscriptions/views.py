from django.shortcuts import render

# Create your views here.

def subscribe(request):
    if request.POST:
        # get first name, last name and email from the post request
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        print(f"POST REQUEST {email = } {firstname = } {lastname = }")

    context = {}
    return render(request, 'subscriptions/subscribe.html', context)