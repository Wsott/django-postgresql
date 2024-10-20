from django.contrib import admin
from .models import Producto, Resenna


# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fabricante', 'precio', 'categoria')


class ResennaAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'usuario', 'comentario', 'puntuacion', 'creacion')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Resenna, ResennaAdmin)
