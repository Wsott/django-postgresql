from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signin', views.registrarse, name='signin'),
    path('perfil/<slug:slug>', views.perfil, name='perfil'),
    path('mi-perfil', views.perfil, name='perfil')
]
