from django.shortcuts import render

# Create your views here.

def subscribe(request):
    context = {}

    if request.POST:

        # get first name, last name and email from the post request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        print(f"POST REQUEST {email = } {first_name = } {last_name = }")

        # check for errors
        errors = []
        if email == "":
            errors.append("Email is required")
        if first_name == "":
            errors.append("First name is required")
        if last_name == "":
            errors.append("Last name is required")
        context["errors"] = errors

    return render(request, 'subscriptions/subscribe.html', context)