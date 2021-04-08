from django.urls import path
from . import views as st


urlpatterns = [
    path('update/', st.updateStatus, name="upstatus"),
]