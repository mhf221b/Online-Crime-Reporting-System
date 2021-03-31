from . import views as lv
from django.urls import path
from user import views as uv

urlpatterns = [
    path('lawagency/', lv.lawagency, name="lawagency"),
]