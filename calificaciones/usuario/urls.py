from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('sign_in/', views.registrarse, name='sign_in'),
]