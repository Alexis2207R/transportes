from django.contrib import admin
from .models import Solicitante

class SolicitanteAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion_solicitante', 'modificacion_solicitante')

admin.site.register(Solicitante, SolicitanteAdmin)
