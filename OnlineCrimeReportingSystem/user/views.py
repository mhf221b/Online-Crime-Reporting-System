from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import GenUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from crimereports.models import Crimereports
from status.models import Status
from django.contrib.auth.backends import BaseBackend
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
            try:

                us = User(first_name=dict['fname'],
                      last_name=dict['lname'],
                      nid=dict['nid'],
                      email=dict['email'],
                      home_address=dict['haddress'],
                      gender=dict['gender'],
                      mobile_number=dict['mnumber'],
                      password=dict['psw'])
                us.save()
            except:
                error = "Invalid Information Given, check again!"
                return render(request, 'user/UserRegForm.html', {'error': error})

            return redirect('home')

        else:
            errorm = "Sorry, Password didn't match"

            return render(request, 'user/UserRegForm.html', {'errorm':errorm})


    return render(request, 'user/UserRegForm.html' )

# def userlogin(request):
#     if request.method == 'POST':
#         dict = request.POST
#         user = User.objects.all()
#         try:
#             if(user.get(nid=dict['nid']) and user.get(password=dict['password'])):
#                 return render(request, 'defaultAdmin/home.html')
#         except:
#             error = "Invalid information"
#             return render(request, 'user/userLogin.html', {'error':error})
#         nid = dict['username']
#         password = dict['password']
#     else:
#     # return redirect()
#         return render(request, 'user/userLogin.html')


def userRegistration(request):
    if request.method=='POST':
        dict = request.POST
        username = dict['username']
        fname = dict['fname']
        lname = dict['lname']
        nid = dict['nid']
        email = dict['email']
        haddress = dict['haddress']
        gender = dict['gender']
        password = dict['psw']
        mnumber = dict['mnumber']
        if(dict['psw']==dict['psw-repeat']):
            try:
                us = User.objects.create_user(password=password, username=username, email = email, first_name=fname, last_name=lname)
                us.save()

                usr = GenUser(user=us, nid = nid, home_address=haddress, gender=gender, mobile_number=mnumber)
                usr.save()
                usrauth = authenticate(username=username, password=password)
                login(request,usrauth)
                return redirect('userprofile')
            except:
                error = "Failed, Please Provide Valid information and try again!"
                return render(request, 'user/UserRegForm.html', {'error':error})

    return render(request, 'user/UserRegForm.html')
@login_required(login_url='uslogin')
def userprofile(request):
    usr = GenUser.objects.all()
    return render(request, 'user/profile.html', {'usr':usr})

def userLogin(request):
    if request.method=='POST':
        dict = request.POST
        username = dict['username']
        password = dict['password']
        try:
            user = authenticate(username=username, password=password)
            us = GenUser.objects.get(user=user)
            if(us.user.username == username):
                login(request, user)
                return redirect('userprofile')
        except:
            error = 'Invalid Information'
            return render(request, 'user/userLogin.html', {'error':error})
    else:
        # error = 'Invalid Information'
        return render(request, 'user/userLogin.html')


def viewReports(request):
    cr = Crimereports.objects.all()
    gu = GenUser.objects.all()

    return render(request, 'user/reports.html', {'cr':cr, 'gu':gu})

def logOut(request):
    auth.logout(request)
    return redirect('Home')

def checkStatus(request):
    cr = Crimereports.objects.all()
    gu = GenUser.objects.all()
    st = Status.objects.all()

    return render(request, 'user/checkstatus.html', {'cr':cr, 'gu':gu, 'st':st})

def updateUser(request):
    if request.method == 'POST':
        dict = request.POST
        username = dict['username']
        fname = dict['fname']
        lname = dict['lname']
        nid = dict['nid']
        email = dict['email']
        haddress = dict['haddress']
        gender = dict['gender']
        password = dict['psw']
        mnumber = dict['mnumber']
        if (dict['psw'] == dict['psw-repeat']):
            try:
                us = User.objects.get(username=username)
                GenUser.objects.filter(user=us).update(nid=nid, home_address=haddress, gender=gender, mobile_number=mnumber)
                return redirect('userprofile')
            except:
                error = "Failed, Please Provide Valid information and try again!"
                return render(request, 'user/UserUpdateForm.html', {'error': error})

    return render(request, 'user/UserUpdateForm.html')

