from django.shortcuts import render
from .models import Status

# Create your views here.

def ss(request):

    status = Status.objects.all()

    return render(request, 'status/Status.html', {'status': status})
