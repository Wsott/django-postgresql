from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from core.forms import SignInForm, LogInForm
from usuario.models import Usuario
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def registrarse(request):
    mensaje_error = None

    if request.method == 'POST':
        datos = SignInForm(request.POST)

        if datos.is_valid():
            try:
                nuevo_usuario = Usuario.objects.get(_nombre=datos.cleaned_data['nombre'])

                mensaje_error = f"Este nombre de usuario ({nuevo_usuario.get_nombre()}) ya esta en uso"
            except ObjectDoesNotExist:
                nuevo_usuario = Usuario()
                nuevo_usuario.set_nombre(datos.cleaned_data['nombre'])
                nuevo_usuario.set_contrasenna(datos.cleaned_data['contrasenna'])
                nuevo_usuario.set_email(datos.cleaned_data['email'])
                nuevo_usuario.save()
                nuevo_usuario.generar_slug()
                return HttpResponse('Exito')
        else:
            mensaje_error = 'El nombre de usuario o contraseña no puede contener espacios'

    return render(request, 'sign_in.html', {
        'titulo': 'Registro de nuevo usuario',
        'form': SignInForm(),
        'error': mensaje_error
    })


def login(request):
    mensaje_error = None

    if request.method == 'POST':
        datos = LogInForm(request.POST)

        if datos.is_valid():
            try:
                usuario = Usuario.objects.get(_nombre=datos.cleaned_data['nombre'])
                if usuario and usuario.iniciar_sesion(datos.cleaned_data['contrasenna']):
                    request.session['usuario_actual'] = {
                        'nombre': usuario.get_nombre(),
                        'id': usuario.id
                    }
                    return redirect('perfil')
                else:
                    mensaje_error = 'Error al iniciar sesion, verifique que su usario y contraseña sean correctos'
            except ObjectDoesNotExist:
                mensaje_error = 'Error al iniciar sesion, verifique que su usario y contraseña sean correctos'
        else:
            mensaje_error = 'Verifique que el usuario y la contraseña no tengan espacios'

    return render(request, 'login.html', {
        'titulo': 'Iniciar sesion',
        'form': LogInForm(),
        'error': mensaje_error
    })


def perfil(request):
    contexto = {
        'usuario': Usuario.objects.get(pk=request.session['usuario_actual']['id'])
    }

    return render(request, 'perfil.html', contexto)
