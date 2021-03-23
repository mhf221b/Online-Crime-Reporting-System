from . import views
from django.urls import path

urlpatterns = [
    path('profile/', views.profile),
    path('register/', views.register),
]