from django.shortcuts import render, redirect
from .models import Status
from crimereports.models import Crimereports
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def ss(request):

    status = Status.objects.all()

    return render(request, 'status/Status.html', {'status': status})

# @login_required
def updateStatus(request):
    if request.method=='POST':
        dict = request.POST
        crimeid = dict['crimeid']
        status = dict['status']
        dou = dict['dou']
        try:
            cr = Crimereports.objects.get(id=crimeid)
            st = Status(user=cr, complaint_status=status, date=dou)
            st.save()
            return redirect('lawprofile')
        except:
            error = "Invalid Information, Check again!"
            return render(request, 'status/updatestatus.html', {'error':error})

    return render(request, 'status/updatestatus.html')
