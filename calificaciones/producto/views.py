from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto


# Create your views here.
def info(request, slug):
    if slug:
        try:
            producto = Producto.objects.get(_slug=slug)
            resennas = producto.resennas.all()

            contexto = {
                'producto': producto,
                'resennas': resennas
            }
            return render(request, 'producto.html', contexto)

        except ObjectDoesNotExist:
            return HttpResponse('Error')
