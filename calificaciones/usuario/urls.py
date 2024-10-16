from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('log_in/', views.login, name='log_in'),
    path('sign_in/', views.registrarse, name='sign_in'),
]