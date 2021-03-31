from . import views as lv
from django.urls import path
from user import views as uv

urlpatterns = [
    path('database/', lv.lawagency, name="lawagency"),
]