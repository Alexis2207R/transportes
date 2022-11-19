from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Pecosa, PecosaMaterial, Material, Entrada, EntradaMaterial, Merma, MermaMaterial

######################################################################

class PecosaResource(resources.ModelResource):
    class Meta:
        model = Pecosa

class MaterialResource(resources.ModelResource):
    class Meta:
        model = Material
        widgets = {
                'creacion_material': {'format': '%d/%m/%Y'},
                'modificacion_material': {'format': '%d/%m/%Y'},
                }

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
    exclude         = ('precio_total_material',)

class MaterialAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields   = ('nombre_material', 'codigo_material')
    list_display    = ('nombre_material', 'codigo_material',  'categoria_material', 'unidad_material', 'ubicacion_material', 'stock_material', 'marca', 'precio_unitario', 'creacion_material')
    resource_class  = MaterialResource
    list_filter     = ('categoria_material', 'creacion_material')
    list_per_page   = 15
    exclude         = ('stock_material',)
    readonly_fields = ('creacion_material', 'modificacion_material')

########################################################################

class EntradaAdmin(admin.ModelAdmin):
    inlines = [EntradaMaterialInline,]
    list_display = ('descripcion_entrada', 'materiales', 'creacion_entrada')
    list_per_page   = 15
    def materiales(self, obj):
        return "\n".join([m.nombre_material for m in obj.matentrada.all()])
    ordering = ('creacion_entrada',)
    readonly_fields = ('creacion_entrada', 'modificacion_entrada')

class MermaAdmin(admin.ModelAdmin):
    inlines = [MermaMaterialInline,]
    list_display = ('descripcion_merma', 'materiales', 'creacion_merma')
    list_per_page   = 15
    def materiales(self, obj):
        return "\n".join([m.nombre_material for m in obj.matmerma.all()])
    ordering = ('creacion_merma',)
    readonly_fields = ('creacion_merma', 'modificacion_merma')

class PecosaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    inlines = [PecosaMaterialInline,]
    list_per_page   = 15
    exclude         = ('precio_total_pecosa',)
    resource_class = PecosaResource

    # Solucionar el problema de las busquedas
    # search_fields = ('solicitante',)
    
    readonly_fields = ('creacion_pecosa', 'modificacion_pecosa')
    list_display = ('descripcion_pecosa', 'materiales', 'precio_total_pecosa', 'solicitante', 'creacion_pecosa')
    def materiales(self, obj):
        return "\n".join([m.nombre_material for m in obj.matpecosa.all()])
    # def costo_total_material(self, obj):
    #     return "\n".join([mp.precio_total_material for mp in obj.precio_total_material.all()])
    ordering = ('creacion_pecosa',)
    list_filter = ('creacion_pecosa',)

admin.site.register(Pecosa, PecosaAdmin)
admin.site.register(Merma, MermaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material, MaterialAdmin)