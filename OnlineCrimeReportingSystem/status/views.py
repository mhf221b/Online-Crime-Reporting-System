from django.shortcuts import render
from .models import Status
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def ss(request):

    status = Status.objects.all()

    return render(request, 'status/Status.html', {'status': status})
