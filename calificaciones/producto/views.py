import math
from types import NoneType

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
                'promedio': 0 if datos_calculados['promedio'] is not NoneType else round(datos_calculados['promedio'], 1)
            }
            return render(request, 'producto.html', contexto)

        except ObjectDoesNotExist:
            return HttpResponse('Error')


def explorar(request):
    cantidad_indices = int(math.ceil(len(Producto.objects.all())/8))
    return render(request, 'explorar.html', {
        'cantidad_indices': cantidad_indices
    })


@csrf_exempt
def api_lista_productos(request, indice, filtro):
    # Si hay 20 elementos
    #
    # [00, 01, 02, 03, 04, 05, 06, 07] => i:1 => [0: 8 ]
    # [08, 09, 10, 11, 12, 13, 14, 15] => i:2 => [9: 16]
    # [16, 17, 18, 19, 20]             => i:3 => [17:  ]
    #
    # Max_i = int(math.ceil(len(Producto.objects.all()) / 8))
    # Primer caso => [: 8]              => i == 1
    # Base seria  => [(8*i)-8 : i*8]    => i != 1 and i != Max_i
    # Ultimo caso => [: 8 * i - 7]      => i == Max_i

    elementos = Producto.objects.all().values('id', '_nombre', '_categoria', '_slug')
    max_i = int(math.ceil(len(elementos) / 8))

    if indice == 1:
        resultados = elementos[:8]
    elif indice == max_i:
        resultados = elementos[(8 * max_i) - 7:]
    else:
        resultados = elementos[(8 * indice) - 8: indice * 8]

    return JsonResponse(resultados, safe=False)



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
