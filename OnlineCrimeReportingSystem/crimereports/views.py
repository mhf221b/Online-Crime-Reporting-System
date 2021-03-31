from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Crimereports
# Create your views here.

@login_required
def cr(request):

    crimereports = Crimereports.objects.all()

    return render(request, 'crimereports/Crimereports.html', {'crimereports': crimereports})


