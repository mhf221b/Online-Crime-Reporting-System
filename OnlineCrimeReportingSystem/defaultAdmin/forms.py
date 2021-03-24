from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',

        ]