from django.http import HttpResponse
from django.template import loader


# Create your views here.
def registrarse(request):
    template = loader.get_template('sign_in.html')
    return HttpResponse(template.render())
