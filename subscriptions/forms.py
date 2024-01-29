from django import forms
from subscriptions.models import Subscriber

# def validate_no_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("This value cannot include a comma")
    
# form for subscriber
class SubscriberForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=50, required=True, help_text="Enter characters only", validators=[validate_no_comma])
    # last_name = forms.CharField(max_length=50, required=True, validators=[validate_no_comma])
    # email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = Subscriber
        fields = "__all__"
        # fields = ['first_name', 'last_name', 'email']

    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if '@' in data:
    #         raise forms.ValidationError("Invalid First Name, cannot include @")