"""CrossCheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from CrossCheck import views as Crosscheck_views

urlpatterns = [

    path('',Crosscheck_views.home,name='home'),
    path('admin/',admin.site.urls),
    path('temp1/',include("temp1.urls")),
    path('semesters/',include("semesters.urls")),
    #path('semesters/',include("app_name.urls", namespace='app_name')),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)