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
    search_fields   = ('nombre_material'),
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
    readonly_fields = ('creacion_pecosa', 'modificacion_pecosa')


admin.site.register(Pecosa, PecosaAdmin)
admin.site.register(Merma, MermaAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Material, MaterialAdmin)