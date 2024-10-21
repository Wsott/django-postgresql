from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


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
    _nombre = models.CharField(max_length=32, unique=True)
    _contrasenna = models.CharField(max_length=256)
    _fecha_creacion = models.DateField(default=timezone.now().date(), editable=False)
    _ultimo_login = models.DateField(default=None, null=True)
    _email = models.EmailField(default=None, null=False, unique=True)
    _slug = models.SlugField(default='', null=False, unique=True)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def ultimo_login(self):
        return self._ultimo_login

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    def set_contrasenna(self, contrasenna):
        """
        Recibe una contraseña la cual se utilizara para generar un hash.

        :type contrasenna: str
        :param contrasenna: Valor que sera utilizado como contraseña.

        :rtype: bool
        :return: Devuelve True si la operacion se creo con exito o False si fallo
        """

        self._contrasenna = make_password(contrasenna)

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
        self.save()

    @property
    def slug(self):
        return self._slug

    def generar_slug(self):
        if not self._slug:
            self._slug = slugify(f'{self._nombre}-{self.pk}')
            self.save()

    def __str__(self):
        return f'ID:{self.pk}. {self._nombre}'
