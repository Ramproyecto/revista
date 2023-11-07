"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

Ejemplo tarea

from django.contrib import admin
from django.urls import path
from core import views as core_views
from blog import views as blog_views

urlpatterns = [
    path('',core_views.Home,name='inicio'),
    path('about/',core_views.AboutUs,name='inicio'),
    path('rooms/',core_views.Rooms,name='inicio'),
    path('blog/',blog_views.Blog,name='blog'),
    path('admin/', admin.site.urls),
    
]


"""
from django.contrib import admin
from core import views as core_views
from django.urls import path

urlpatterns = [
    path('',core_views.Home,name='inicio'),
    path('about/', core_views.AboutUs, name='nosotros'),
    path('admin/', admin.site.urls),
]
