from django.db import models


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
