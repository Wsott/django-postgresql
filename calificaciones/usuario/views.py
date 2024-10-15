from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from core.forms import SignInForm
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

    template = loader.get_template('sign_in.html')
    return render(request, 'sign_in.html', {'form': SignInForm()})
    #return HttpResponse(template.render())
