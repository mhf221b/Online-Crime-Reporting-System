from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Crimereports
from user.models import GenUser
# Create your views here.

@login_required
def cr(request):

    crimereports = Crimereports.objects.all()

    return render(request, 'crimereports/Crimereports.html', {'crimereports': crimereports})

def reportCrime(request):
    if request.method=='POST':
        dict = request.POST
        nid = dict['nid']
        crimeid= dict['crimeid']
        loc= dict['loc']
        toc= dict['toc']
        doc = dict['doc']
        cd= dict['cd']
        try:
            gu = GenUser.objects.get(nid=nid)
            cr = Crimereports(user=gu, crime_id=crimeid, location_of_crime=loc, type_of_crime=toc, date_of_crime=doc, crime_description=cd)
            cr.save()
            return redirect('userprofile')
        except:
            error = "Sorry, Wrong Information Given, Try Again"
            return render(request, 'crimereports/ReportingCrime.html', {'error': error})
    else:
                return render(request, 'crimereports/ReportingCrime.html')



