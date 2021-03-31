from . import views as uv
from django.urls import path


urlpatterns = [
    path('user/', uv.userdatabase, name="user"),
]