from django.contrib import admin
from django.utils.html import format_html
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from import_export.admin import ImportExportModelAdmin
from .models import Pecosa, PecosaMaterial, Material, Entrada, EntradaMaterial, Merma, MermaMaterial, Categoria, Unidad

######################################################################

class PecosaAdminResource(resources.ModelResource):

    codigo_material = fields.Field(column_name='codigo_material', attribute='matpecosa', widget=ManyToManyWidget(Material, field='codigo_material'))
    materiales = fields.Field(column_name='materiales', attribute='matpecosa', widget=ManyToManyWidget(Material, field='nombre_material'))
    precio_unitario = fields.Field(column_name='precio_unitario', attribute='matpecosa', widget=ManyToManyWidget(Material, field='precio_unitario'))
    solicitante = fields.Field(column_name='solicitante', attribute='solicitante', widget=ForeignKeyWidget(Unidad, field='nombre_solicitante'))

    class Meta:
        model = Pecosa
        fields =    (
                    'descripcion_pecosa',
                    'solicitante',
                    'codigo_material',
                    'materiales',
                    'precio_unitario',
                    'precio_total_pecosa',
                    'creacion_pecosa',
                    )
        exclude = ('id',)
        export_order =  (
                        'descripcion_pecosa',
                        'solicitante',
                        'codigo_material',
                        'materiales',
                        'precio_unitario',
                        'precio_total_pecosa',
                        'creacion_pecosa',
                        )
        widgets = {
                'creacion_pecosa': {'format': '%d/%m/%Y'},
                'modificacion_pecosa': {'format': '%d/%m/%Y'},
                }
        

class MaterialAdminResource(resources.ModelResource):

    categoria = fields.Field(column_name='categoria_material', attribute='categoria_material', widget=ForeignKeyWidget(Categoria, field='nombre_categoria'))
    unidad = fields.Field(column_name='unidad_material', attribute='unidad_material', widget=ForeignKeyWidget(Unidad, field='nombre_unidad'))

    class Meta:
        model = Material
        fields = (
                'nombre_material',
                'codigo_material',
                'precio_unitario',
                'categoria',
                'unidad',
                'ubicacion_material',
                'stock_material',
                'creacion_material',
                )
        exclude = ('id',)
        export_order =  (
                        'nombre_material',
                        'codigo_material',
                        'precio_unitario',
                        'categoria',
                        'unidad',
                        'ubicacion_material',
                        'stock_material',
                        'creacion_material',
                        )
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
    resource_class  = MaterialAdminResource
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
        return format_html("</br>".join([m.nombre_material for m in obj.matentrada.all()]))
    ordering = ('creacion_entrada',)
    readonly_fields = ('creacion_entrada', 'modificacion_entrada')

class MermaAdmin(admin.ModelAdmin):
    inlines = [MermaMaterialInline,]
    list_display = ('descripcion_merma', 'materiales', 'creacion_merma')
    list_per_page   = 15
    def materiales(self, obj):
        return format_html("</br>".join([m.nombre_material for m in obj.matmerma.all()]))
    ordering = ('creacion_merma',)
    readonly_fields = ('creacion_merma', 'modificacion_merma')

class PecosaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    inlines = [PecosaMaterialInline,]
    list_per_page   = 15
    exclude         = ('precio_total_pecosa',)
    resource_class = PecosaAdminResource
    
    readonly_fields = ('creacion_pecosa', 'modificacion_pecosa')
    list_display = ('descripcion_pecosa', 'materiales', 'precio_unitario', 'precio_total_pecosa', 'solicitante', 'creacion_pecosa')

    def precio_unitario(self, obj):
        return format_html("</br>".join([str(p.precio_unitario) for p in obj.matpecosa.all()]))

    def materiales(self, obj):
        return format_html("</br>".join([m.nombre_material for m in obj.matpecosa.all()]))
    ordering = ('creacion_pecosa',)
    list_filter = ('creacion_pecosa',)

admin.site.register(Pecosa, PecosaAdmin)
admin.site.register(Merma, MermaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material, MaterialAdmin)