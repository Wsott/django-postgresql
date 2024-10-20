from django.urls import path

from . import views


urlpatterns = [
    path('info/<slug:slug>', views.info, name='info'),
    path('api/<int:producto_id>/<int:max>/<str:orden>', views.api_listar_resennas, name='api_listar_resennas')
]
