from django.db import models
from django.utils import timezone


# Create your models here.
class Usuario(models.Model):
    """
    Modelo que representa a los usuarios registrados en el sistema. Todos sus atributos son
    privados y solamente accedibles mediante los metodos correspondientes del tipo get_[atributo].
    Estos metodos permiten acceder de forma correcta a la informacion.

    Similar a lo anterior, para cambiar la informacion almacenada del registro es necesario utilizar
    los metodos set_[atributo] y pasarle los parametros correctos.

    :ivar nombre: Nombre de usuario, longitud maxima de 32 caracteres
    :vartype nombre: str

    :ivar fecha_creacion: Fecha en la que se creo el registro en el sistema. Solo lectura.
    :vartype fecha_creacion: date

    :ivar ultimo_login: Fecha del ultimo inicio de sesion en el sistema. Actualizacion automatica. Solo lectura.
    :vartype ultimo_login: date
    """
    _nombre = models.CharField(max_length=32)
    _contrasenna = models.CharField(max_length=256)
    _fecha_creacion = models.DateField(default=timezone.now().date(), editable=False)
    _ultimo_login = models.DateField(default=None, null=True)
