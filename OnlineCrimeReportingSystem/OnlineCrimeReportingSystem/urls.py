"""OnlineCrimeReportingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from defaultAdmin import views as dAviews
from history import views as hv

from django.conf import settings
from django.conf.urls.static import static

from lawagency import views as lv

from crimereports import views as cv
from status import views as dv
urlpatterns = [
    # path('', dAviews.home),
    path('admin/', admin.site.urls),
    path('admins/', include('defaultAdmin.urls')),
    path('accounts/profile/', dAviews.profile, name="Profile"),
    path('database/', include('lawagency.urls')),
    path('database/', include('user.urls')),
    path('database/', include('crimereports.urls')),
    path('crimereports/', include('crimereports.urls')),
    path('database/', include('status.urls')),
    path('status/', include('status.urls')),
    path('user/', include('user.urls')),
    path('lawagency/', include('lawagency.urls')),
    path('', dAviews.basehome, name="Home"),
    path('history/', hv.profilepic, name = "Propic"),
    path('history/update', hv.profile_update, name = "PropicUpdate"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
