from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from core.forms import SignInForm, LogInForm
from usuario.models import Usuario


# Create your views here.
def registrarse(request):
    if request.method == 'POST':
        datos = SignInForm(request.POST)

        if datos.is_valid():
            nuevo_usuario = Usuario()
            nuevo_usuario.set_nombre(datos.cleaned_data['nombre'])
            nuevo_usuario.set_contrasenna(datos.cleaned_data['contrasenna'])
            nuevo_usuario.save()
            return HttpResponse('Exito')
        else:
            return HttpResponse('Error')

    return render(request, 'sign_in.html', {
        'titulo': 'Registro de nuevo usuario',
        'form': SignInForm()})


def login(request):
    if request.method == 'POST':
        datos = LogInForm(request.POST)

        if datos.is_valid():
            usuario = Usuario.objects.get(_nombre=datos.cleaned_data['nombre'])
            if usuario and usuario.iniciar_sesion(datos.cleaned_data['contrasenna']):
                return HttpResponse('Iniciada sesion')
            else:
                return HttpResponse('Error al iniciar sesion')
        else:
            return HttpResponse('Error')

    return render(request, 'login.html', {
        'titulo': 'Iniciar sesion',
        'form': LogInForm()
    })