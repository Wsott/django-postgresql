from django.urls import path

from . import views


urlpatterns = [
    path('info/<slug:slug>', views.info, name='info'),
    path('explorar', views.explorar, name='explorar'),
    path('api/<int:producto_id>/<int:max>/<str:orden>', views.api_listar_resennas, name='api_listar_resennas'),
    path('api/<int:indice>/<str:filtro>', views.api_lista_productos, name='lista_productos')
]
