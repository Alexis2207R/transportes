from django.contrib import admin
from .models import Solicitante, Area

class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ('nombre_solicitante', 'area', 'sexo_solicitante', 'telefono_solicitante', 'creacion_solicitante')
    readonly_fields = ('creacion_solicitante', 'modificacion_solicitante')

class AreaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion_area', 'modificacion_area')

admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Area, AreaAdmin)
