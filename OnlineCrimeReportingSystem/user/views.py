from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.decorators import login_required
from user.forms import UserReg
# Create your views here.


@login_required
def userdatabase (request):
    var = User.objects.all()
    # return render(request, 'user/usersinfo.html', {'user': user})
    return  render(request, 'user/usersinfo.html', {'var': var})

def userreg(request):
    if (request.method=='POST'):
        dict = request.POST

        if(dict['psw']==dict['psw-repeat']):
            print(dict['gender'])
            us = User(first_name=dict['fname'],
                      last_name=dict['lname'],
                      nid=dict['nid'],
                      email=dict['email'],
                      home_address=dict['haddress'],
                      gender=dict['gender'],
                      mobile_number=dict['mnumber'],
                      password=dict['psw'])
            us.save()

            return redirect('home')

        else:
            errorm = "Sorry, Password didn't match"

            return render(request, 'user/UserRegForm.html', {'errorm':errorm})


    return render(request, 'user/UserRegForm.html' )


