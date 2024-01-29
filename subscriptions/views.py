from django.shortcuts import render
from subscriptions.forms import SubscriberForm
from subscriptions.models import Subscriber

# Create your views here.

def subscribe(request):
    subscribe_form = SubscriberForm()

    if request.POST:
        subscribe_form = SubscriberForm(request.POST) # bound

        if subscribe_form.is_valid():
            print(f"VALID FORM {subscribe_form.first_name = } {subscribe_form.last_name = } {subscribe_form.email = }")

            #     # save the subscriber to the database
            #     subscriber = Subscriber(first_name=first_name, last_name=last_name, email=email)
            #     subscriber.save()

    context = { "form" : subscribe_form }
    return render(request, 'subscriptions/subscribe.html', context)

def subscribe_manual(request):
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

        if len(errors) == 0:
            # save the subscriber to the database
            subscriber = Subscriber(first_name=first_name, last_name=last_name, email=email)
            subscriber.save()

    return render(request, 'subscriptions/subscribe.html', context)