from django.db import models
from django.utils import timezone


# Create your models here.
class Usuario(models.Model):
    """
    Modelo que representa a los usuarios registrados en el sistema. Todos sus atributos son
    privados y solamente accedibles mediante los metodos correspondientes del tipo get_[atributo].
    Estos metodos permiten acceder de forma correcta a la informacion.

    Similar a lo anterior, para definir la informacion almacenada del registro es necesario utilizar
    los metodos set_[atributo] y pasarle los parametros correctos.

    Para actualizar los datos, sera necesario utilizar los metodos update_[atributo] y pasarle los datos
    correspondientes.

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

    def _validar_nombre(self, nombre):
        """
        Funcion de uso interno para validar que el nombre de usuario se adecua a lo necesario.

        Debera: ser str, no tener mas de 32 caracteres, no tener espacios en blanco.

        :type nombre: str
        :param nombre: Valor que sera evaluado.

        :rtype: bool
        :return: Devuelve True si es valido o False si es invalido
        """

        if isinstance(nombre, str):
            if len(nombre) < 32:
                if not ' ' in nombre:
                    self._nombre = nombre
                    return True

        return False

    def set_nombre(self, nombre):
        """
        Recibe una cadena de texto que sera el nombre de usuario. Solamente se puede realizar el set
        la primera vez, posterioremente es necesario utilizar la funcion update_nombre

        :type nombre: str
        :param nombre: Nombre del usuario.

        :rtype: bool
        :return: Devuelve True si la operacion se completo con exito. False si la operacion fallo.
        """

        if not self._nombre and self._validar_nombre(nombre):
            self._nombre = nombre
            return True

        return False

    def get_nombre(self):
        """
        Devuelve el nombre de usuario del registro representado por la instancia.

        :rtype: str | None
        """

        return self._nombre if self._nombre is not '' else None

    def update_nombre(self, nombre):
        """
        Actualiza el nombre de usuario previamente definido.

        :type nombre: str
        :param nombre: Valor al cual se actualizara el nombre de usuario.

        :rtype: bool
        :return: Devuelve True si la operacion se completo con exito o False si fallo.
        """

        if self._nombre and self._validar_nombre(nombre):
            self._nombre = nombre
            return True

        return False
