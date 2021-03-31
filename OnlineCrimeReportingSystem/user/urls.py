from . import views as uv
from django.urls import path


urlpatterns = [
    path('database/', uv.userdatabase, name="user"),
]