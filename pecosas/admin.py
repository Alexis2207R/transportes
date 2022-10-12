from django.contrib import admin
from .models import Pecosa, PecosaMaterial, Material

class PecosaMaterialInline(admin.TabularInline):
    model   = PecosaMaterial
    extra   = 1

class PecosaAdmin(admin.ModelAdmin):
    inlines = [PecosaMaterialInline,]
    readonly_fields = ('creacion_pecosa', 'modificacion_pecosa')

admin.site.register(Pecosa, PecosaAdmin)
