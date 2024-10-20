from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Producto


# Create your views here.
def info(request, slug):
    if slug:
        try:
            producto = Producto.objects.get(_slug=slug)
            resennas = producto.resennas.order_by('-_creacion')[:5]
            datos_calculados = producto.resennas.aggregate(promedio=Avg('_puntuacion'), cantidad=Count('id'))

            contexto = {
                'producto': producto,
                'resennas': resennas,
                'cantidad_resennas': datos_calculados['cantidad'],
                'promedio': round(datos_calculados['promedio'], 1)
            }
            return render(request, 'producto.html', contexto)

        except ObjectDoesNotExist:
            return HttpResponse('Error')


@csrf_exempt
def api_listar_resennas(request, producto_id=None, max=5, orden=None):
    resultados = None

    if producto_id:
        producto = Producto.objects.get(pk=producto_id)

        resultados = producto.resennas.select_related('usuario').order_by(orden).values(
            '_usuario___nombre', '_usuario___slug', '_titulo', '_comentario', '_puntuacion', '_creacion')[:max]

        #print(resultados[1])

        #listado = list(resultados.values('_usuario', '_comentario', '_puntuacion', '_creacion'))

    return JsonResponse(list(resultados), safe=False)
