from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AdminRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, authenticate, login
from django.contrib.auth.models import User
from user.forms import UserReg
from lawagency.models import LawAgency


# Create your views here.
@login_required(login_url='lawlogin')
def home(request):
    la = LawAgency.objects.all()
    us = User.objects.all()
    return render(request, 'defaultAdmin/home.html', {'la':la, 'us':us})

@login_required(login_url='login')
def profile(request):
    return render(request, 'defaultAdmin/profile.html')


def register(request):
    if request.method=='POST':
        reg_form = AdminRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get('username')
            password = reg_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        reg_form = AdminRegistrationForm()

    context = {
        'form': reg_form,
        }
    return render(request, 'defaultAdmin/register.html', context)

def basehome(request):
    return render(request, 'defaultAdmin/homebasetrial1.html')