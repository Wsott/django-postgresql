from django.contrib import admin
from .models import Usuario


# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', '_nombre', '_fecha_creacion', '_ultimo_login', '_email', '_slug')


admin.site.register(Usuario, UsuarioAdmin)
