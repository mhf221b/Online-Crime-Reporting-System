from django.urls import path
from . import views as crv

urlpatterns = [
    path('crimereports/', crv.cr, name="crimereports"),
]