from django.contrib import admin
from .models import Categoria, Material, Unidad

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion_categoria', 'modificacion_categoria')

class UnidadAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion_unidad', 'modificacion_unidad')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Unidad, UnidadAdmin)