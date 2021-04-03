from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='defaultAdmin/login.html'), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='defaultAdmin/logout.html'), name = 'logout'),

]