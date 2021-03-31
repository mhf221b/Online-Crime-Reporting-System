from django.shortcuts import render

from .models import Crimereports
# Create your views here.

def cr(request):

    crimereports = Crimereports.objects.all()

    return render(request, 'crimereports/Crimereports.html', {'crimereports': crimereports})


