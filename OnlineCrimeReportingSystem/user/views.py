from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def userdatabase (request):
    var = User.objects.all()
    # return render(request, 'user/usersinfo.html', {'user': user})
    return  render(request, 'user/usersinfo.html', {'var': var})

