from . import views as lv
from django.urls import path

urlpatterns = [
    path('lawagency/', lv.lawagency, name="lawagency"),
    path('registration/', lv.lawreg, name="lawsignup"),
    path('login/', lv.lawLogin, name = "lawlogin"),
    path('profile/', lv.lawprofile, name="lawprofile"),
    path('reports/', lv.checkReports, name="lawreport"),
    path('updatestatus/', lv.updateStatus, name="updatestatus"),
    path('checkstatus/', lv.checkStatus, name="checkLawstatus"),
    path('update/', lv.lawUpdate, name="updatelaw")

    ]