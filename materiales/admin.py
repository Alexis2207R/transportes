from django.contrib import admin
from .models import Categoria, Material

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion_categoria', 'modificacion_categoria')

class MaterialAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion_material', 'modificacion_material')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Material, MaterialAdmin)