from django.contrib.auth.hashers import make_password, check_password
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
                    return True

        return False

    def _validar_contrasenna(self, contrasenna):
        """
        Funcion interna que evalua si la contraseña es valida.

        Debera: tener al menos 8 caracteres, ser un str y no tener espacios en blanco

        :type contrasenna: str
        :param contrasenna: Parametro que sera evaluado

        :rtype: bool
        :return: Devuelve True si la contraseña es valida o False si no lo es.
        """

        if isinstance(contrasenna, str):
            if len(contrasenna) >= 8:
                if ' ' not in contrasenna:
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

    def set_contrasenna(self, contrasenna):
        """
        Recibe una contraseña la cual se utilizara para generar un hash.

        :type contrasenna: str
        :param contrasenna: Valor que sera utilizado como contraseña.

        :rtype: bool
        :return: Devuelve True si la operacion se creo con exito o False si fallo
        """

        if not self._contrasenna and self._validar_contrasenna(contrasenna):
            self._contrasenna = make_password(contrasenna)
            return True

        return False

    def iniciar_sesion(self, contrasenna):
        """
        Metodo utilizada para validar la contraseña ingresada por el usuario con la almacenada en el sistema.

        :type contrasenna: str
        :param contrasenna: Contraseña ingresada por el usuario

        :rtype: bool
        :return: True si se valido correctamente la contraseña o False si fallo la validacion
        """

        if self._contrasenna:
            if check_password(contrasenna, self._contrasenna):
                self._actualizar_fecha_ultimo_login()
                return True

        return False

    def _actualizar_fecha_ultimo_login(self):
        """
        Metodo interno para actualizar automaticamente la ultima fecha de inicio de sesion.

        :rtype: None
        """
        self._ultimo_login = timezone.now().date()

    def get_ultimo_login(self):
        """
        Metodo que devuelve la fecha del ultimo inicio de sesion. Atributo de solo lectura.

        :rtype: date
        :return: Fecha del ultimo inicio de sesion exitoso.
        """
        return self._ultimo_login

    def get_fecha_creacion(self):
        """
        Devuelve la fecha en la que se registro el usuario en el sistema. Atributo de solo lectura.

        :rtype: date
        :return: Devuelve la fecha de registro.
        """

        return self._fecha_creacion

