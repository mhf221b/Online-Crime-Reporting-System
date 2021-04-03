from django.shortcuts import render, redirect
from .models import LawAgency
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def lawagency(request):

    lawlist = LawAgency.objects.all()
    return render(request, 'lawagency/databaseoflawagency.html', {'lawlist':lawlist})

def lawreg(request):
    if (request.method=='POST'):
        dict = request.POST
        if(dict['psw']==dict['psw-repeat']):
            try:
                la = LawAgency(user_id=dict['userid'],
                           name=dict['name'],
                           email=dict['email'],
                           agency_branch=dict['abranch'],
                           password=dict['psw'])
                la.save()
                return redirect('home')
            except:
                error = "Invalid Information Given, check again!"
                return render(request, 'lawagency/LawRegister.html', {'error': error})
        else:
            errorp = "Password didn't match"
            return render(request, 'lawagency/LawRegister.html', {'errorp':errorp})


    return render(request, 'lawagency/LawRegister.html')

