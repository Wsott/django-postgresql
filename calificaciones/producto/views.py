import math
from types import NoneType

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Producto, Resenna
from core.forms import NuevaResenaForm

from usuario.models import Usuario


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
                'promedio': 0 if datos_calculados['promedio'] is None else round(datos_calculados['promedio'], 1)
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

    if filtro != 'ZZ':
        elementos = Producto.objects.filter(_categoria=filtro).values('id', '_nombre', '_categoria', '_slug')
        cantidad_indices = int(math.ceil(len(elementos) / 8))
    else:
        elementos = Producto.objects.all().values('id', '_nombre', '_categoria', '_slug')
        cantidad_indices = int(math.ceil(len(elementos) / 8))

    max_i = int(math.ceil(len(elementos) / 8))

    if indice == 1:
        resultados = elementos[:8]
    elif indice == max_i:
        resultados = elementos[(8 * max_i) - 7:]
    else:
        resultados = elementos[(8 * indice) - 8: indice * 8]

    respuesta = {
        'cantidad_indices': cantidad_indices,
        'respuesta': resultados
    }

    return JsonResponse(respuesta, safe=False)


def crear_resena(request, slug):
    mensaje_error = None
    producto = Producto.objects.get(_slug=slug)

    if request.method == 'POST':
        datos = NuevaResenaForm(request.POST)

        if datos.is_valid():
            nueva_resena = Resenna()
            nueva_resena.producto = producto
            nueva_resena.usuario = Usuario.objects.get(pk=request.session['usuario_actual']['id'])
            nueva_resena.titulo = datos.cleaned_data['titulo']
            nueva_resena.comentario = datos.cleaned_data['comentario']
            nueva_resena.puntuacion = datos.cleaned_data['puntuacion']
            nueva_resena.save()
            return redirect(f'/producto/info/{producto.slug}')
        else:
            mensaje_error = 'El nombre de usuario o contraseña no puede contener espacios'

    return render(request, 'crear_resena.html', {
        'titulo': 'Nueva reseña para ' + producto.nombre,
        'form': NuevaResenaForm(),
        'slug': slug,
        'error': mensaje_error
    })

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
