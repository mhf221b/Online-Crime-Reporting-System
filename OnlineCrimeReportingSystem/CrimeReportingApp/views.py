from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def run(request):
    return render(request, "CRA/lulu.html")
