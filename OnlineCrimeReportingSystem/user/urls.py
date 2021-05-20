from . import views as uv
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user/', uv.userdatabase, name="user"),
    path('registration/', uv.userRegistration, name="usignup"),
    path('login/', uv.userLogin, name="uslogin"),
    path('profile/', uv.userprofile, name="userprofile"),
    path('viewreports/', uv.viewReports, name="viewreports"),
    path('logout/', uv.logOut, name="userlogout"),
    path('checkstatus/', uv.checkStatus, name="checkstatus"),
    path('update/', uv.updateUser, name="updateuser"),


]