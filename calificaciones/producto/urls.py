from django.urls import path

from . import views


urlpatterns = [
    path('info/<slug:slug>', views.info, name='info'),
]
