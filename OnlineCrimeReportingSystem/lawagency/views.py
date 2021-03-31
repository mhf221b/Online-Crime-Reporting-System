from django.shortcuts import render
from .models import LawAgency
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def lawagency(request):

    lawlist = LawAgency.objects.all()
    return render(request, 'lawagency/databaseoflawagency.html', {'lawlist':lawlist})
