from django.contrib.auth.forms import forms

class UserReg(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=15)
    last_name = forms.CharField(label="Last Name", max_length=15)
    nid = forms.IntegerField(label="NID")
    email_address = forms.CharField(label="Email Address")
    home_address = forms.CharField(label="Home Address")
    gender = forms.ChoiceField(choices=[('1', 'Male'), ('2', 'Female')], widget=forms.RadioSelect)
    mobile_number = forms.CharField(label="Mobile Number", max_length=15)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)