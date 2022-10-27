from django.contrib import admin
from .models import Pecosa, PecosaMaterial, Material, Entrada, EntradaMaterial, Merma, MermaMaterial

######################################################################

class EntradaMaterialInline(admin.TabularInline):
    model   = EntradaMaterial
    extra   = 1
    autocomplete_fields = ['material']

class MermaMaterialInline(admin.TabularInline):
    model   = MermaMaterial
    extra   = 1
    autocomplete_fields = ['material']

class PecosaMaterialInline(admin.TabularInline):
    model   = PecosaMaterial
    extra   = 1
    autocomplete_fields = ['material']

class MaterialAdmin(admin.ModelAdmin):
    search_fields   = ('nombre_material', 'codigo_material')
    list_display    = ('nombre_material','codigo_material',  'categoria_material', 'unidad_material', 'ubicacion_material', 'stock_material', 'marca', 'precio_unitario', 'creacion_material')
    list_filter     = ('categoria_material', 'creacion_material')
    list_per_page   = 15
    exclude         = ('stock_material',)
    readonly_fields = ('creacion_material', 'modificacion_material')

########################################################################

class EntradaAdmin(admin.ModelAdmin):
    inlines = [EntradaMaterialInline,]
    readonly_fields = ('creacion_entrada', 'modificacion_entrada')

class MermaAdmin(admin.ModelAdmin):
    inlines = [MermaMaterialInline,]
    readonly_fields = ('creacion_merma', 'modificacion_merma')

class PecosaAdmin(admin.ModelAdmin):
    inlines = [PecosaMaterialInline,]

    # Solucionar el problema de las busquedas
    # search_fields = ('solicitante',)
    
    readonly_fields = ('creacion_pecosa', 'modificacion_pecosa')
    list_display = ('codigo_pecosa', 'descripcion_pecosa', 'materiales', 'solicitante', 'creacion_pecosa',)
    def materiales(self, obj):
        return "\n".join([m.nombre_material for m in obj.matpecosa.all()])
    ordering = ('creacion_pecosa',)
    list_filter = ('creacion_pecosa',)


admin.site.register(Pecosa, PecosaAdmin)
admin.site.register(Merma, MermaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material, MaterialAdmin)