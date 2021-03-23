from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def profile(request):

    contents = {
        'name': "Mehedi Hasan",
        'ID':"18201042",
        'email': "mhf221b@gmail.com",
    }
    return render(request, 'defaultAdmin/profile.html', contents)


def register(request):
    if request.method=='POST':
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
    else:
        reg_form = UserCreationForm()

    context = {
        'form': reg_form,
        }
    return render(request, 'defaultAdmin/register.html', context)