from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from usuario.models import Usuario


# Create your models here.
class Producto(models.Model):
    class Categoria(models.TextChoices):
        ELECTRONICA = 'EL', 'Electronica'
        COMIDA = 'CO', 'Comida'
        ROPA = 'RO', 'Ropa'
        LIBROS = 'LI', 'Libros'
        JUGUETES = 'JU', 'Juguetes'
        HOGAR = 'HO', 'Hogar'
        OTROS = 'XX', 'Otros'

    _nombre = models.TextField(null=False, unique=True, max_length=32)
    _fabricante = models.TextField(null=False, max_length=32)
    _precio = models.FloatField(null=True)
    _categoria = models.CharField(null=False, max_length=2, choices=Categoria.choices, default=Categoria.OTROS)
    _slug = models.TextField(null=False, unique=True, max_length=72)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, value):
        self._fabricante = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    @property
    def categoria(self):
        return self.get__categoria_display()

    @categoria.setter
    def categoria(self, value):
        if value in dict(Producto.Categoria.choices):
            self._categoria = value
        else:
            raise ValueError(f'{value} no es una categoria valida')

    @property
    def slug(self):
        return self._slug

    def generar_slug(self):
        self._slug = slugify(f'{self.nombre} {self.fabricante} {self.pk}')

    def __str__(self):
        return f'ID:{self.pk}. {self._nombre}'


class Resenna(models.Model):
    _producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='resennas')
    _usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    _titulo = models.TextField(max_length=32, null=False)
    _comentario = models.TextField(max_length=256, null=False)
    _puntuacion = models.IntegerField(default=3)
    _creacion = models.DateField(default=timezone.now().date())

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, value):
        self._producto = value

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value):
        self._usuario = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, value):
        self._comentario = value

    @property
    def puntuacion(self):
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, value):
        if 1 <= int(value) <= 5:
            self._puntuacion = value
        else:
            raise ValueError(f'{value} no es un valor valido')

    @property
    def creacion(self):
        return self._creacion

    def obtener_rango(self):
        return range(0, self.puntuacion)

    def __str__(self):
        return f'ID:{self.pk}. {self.producto.nombre}; {self.usuario._nombre}; {self.puntuacion} estrellas'
