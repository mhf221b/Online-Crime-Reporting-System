from django.shortcuts import render
from .models import Profile

# Create your views here.
def profilepic(request):

    # user = Profile.objects.all()
    return render(request, 'history/history.html')


def profile_update(request):
    return render (request, 'history/history_update.html')