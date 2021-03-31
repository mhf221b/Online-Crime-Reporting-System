from django.urls import path
from . import views as st


urlpatterns = [
    path('status/', st.ss, name="status"),
]