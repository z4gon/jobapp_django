from django.shortcuts import render

# Create your views here.

def subscribe(request):
    context = {}

    if request.POST:

        # get first name, last name and email from the post request
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')

        print(f"POST REQUEST {email = } {firstname = } {lastname = }")

        # check for errors
        errors = []
        if email == "":
            errors.append("Email is required")
        if firstname == "":
            errors.append("First name is required")
        if lastname == "":
            errors.append("Last name is required")
        context["errors"] = errors

    return render(request, 'subscriptions/subscribe.html', context)