from . import views as lv
from django.urls import path

urlpatterns = [
    path('lawagency/', lv.lawagency, name="lawagency"),
    path('registration/', lv.lawreg, name="lawsignup"),
]