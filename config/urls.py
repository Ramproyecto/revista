
from django.contrib import admin
from core import views as core_views
from django.urls import path

urlpatterns = [
    path('',core_views.Home,name='inicio'),
    path('about/', core_views.AboutUs, name='nosotros'),
    path('faq/', core_views.Frequent, name='preguntas_frecuentes'),
    path('revista/', core_views.Magazine, name='revista'),
    path('admin/', admin.site.urls),
]

