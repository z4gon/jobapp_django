from django import forms
# from subscriptions.models import Subscriber

# form for subscriber
class SubscriberForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)

    # class Meta:
    #     model = Subscriber
    #     fields = "__all__"