from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import LawAgency
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from crimereports.models import Crimereports
from status.models import Status

# Create your views here.

@login_required
def lawagency(request):

    lawlist = LawAgency.objects.all()
    return render(request, 'lawagency/databaseoflawagency.html', {'lawlist':lawlist})

def lawreg(request):
    if (request.method=='POST'):
        dict = request.POST
        # propic = dict['propic']
        username = dict['username']
        agencyid = dict['a_id']
        first_name = dict['fname']
        last_name = dict['lname']
        email = dict['email']
        agencybranch = dict['abranch']
        password = dict['psw']
        if(dict['psw']==dict['psw-repeat']):
            try:
                user = User.objects.create_superuser(username=username, first_name = first_name, last_name=last_name,
                                                     email=email, password=password)
                user.save()

                la = LawAgency(user=user, agency_branch=agencybranch, agency_ID=agencyid)
                la.save()
                log = authenticate(username=username, password=password)
                login(request, log)
                return redirect('lawprofile')
            except:
                error = "Invalid Information Given, check again!"
                return render(request, 'lawagency/LawRegister.html', {'error': error})
        else:
            errorp = "Password didn't match"

            return render(request, 'lawagency/LawRegister.html', {'errorp':errorp})


    return render(request, 'lawagency/LawRegister.html')

def lawLogin(request):
    if request.method=='POST':
        dict = request.POST
        username = dict['username']
        password = dict['password']
        user = auth.authenticate(request, username=username, password=password)
        try:
            if user is not None:
                la = LawAgency.objects.get(user=user)
                if la.usertype=='Law Agency':
                    auth.login(request, user)
                    return redirect('lawprofile')
                else:
                    return redirect('lawlogin')
            else:
                return redirect('lawlogin')
        except:
            notagent = "Sorry, invalid information, Try Again!"
            return render(request, 'lawagency/LawAgencyLogin.html', {'notagent':notagent})

    else:
        return render(request, 'lawagency/LawAgencyLogin.html')

def lawlogout(request):
    auth.logout(request)
    return render(request, 'lawagency/logout.html')

def lawprofile(request):
    la = LawAgency.objects.all()
    return render(request, 'lawagency/profile.html', {'la':la})

def checkReports(request):
    cr = Crimereports.objects.all()
    st = Status.objects.all()
    return render(request, 'lawagency/reports.html',{'cr':cr, 'st':st})

def updateStatus(request):
    if request.method=='POST':
        dict = request.POST
        crimeid = dict['crimeid']
        status = dict['status']
        dou = dict['dou']
        try:
            cr = Crimereports.objects.get(crime_id=crimeid)
            Status.objects.filter(user=cr).update(complaint_status=status, date=dou)
            return redirect('lawprofile')
        except:
            error = "Invalid Information Given, Try Again"
            return render(request, 'lawagency/updatestatus.html', {'error':error})
    else:
         return render(request, 'lawagency/updatestatus.html')


def checkStatus(request):
    st = Status.objects.all()
    return render(request, 'lawagency/checkstatus.html', {'st':st})

def lawUpdate(request):
    if (request.method == 'POST'):
        dict = request.POST
        username = dict['username']
        agencyid = dict['a_id']
        first_name = dict['fname']
        last_name = dict['lname']
        email = dict['email']
        agencybranch = dict['abranch']
        password = dict['psw']
        if (dict['psw'] == dict['psw-repeat']):
            try:
                user = User.objects.get(username=username)
                LawAgency.objects.filter(user=user).update(agency_branch=agencybranch)

                # la = LawAgency(user=user, agency_branch=agencybranch, agency_ID=agencyid)
                # la.save()
                log = authenticate(username=username, password=password)
                login(request, log)
                return redirect('lawprofile')
            except:
                error = "Invalid Information Given, check again!"
                return render(request, 'lawagency/LawUpdate.html', {'error': error})
        else:
            errorp = "Password didn't match"

            return render(request, 'lawagency/LawUpdate.html', {'errorp': errorp})

    return render(request, 'lawagency/LawUpdate.html')
