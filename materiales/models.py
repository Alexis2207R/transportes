from django.db import models
from django.utils.timezone import now

class Categoria(models.Model):
    nombre_categoria        = models.CharField(max_length=100, verbose_name="Nombre")
    creacion_categoria      = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_categoria  = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
	  
    def __str__(self):
        	return self.nombre_categoria

class Unidad(models.Model):
    nombre_unidad         = models.CharField(max_length=150, verbose_name="Nombre")
    creacion_unidad       = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_unidad   = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
	  
    def __str__(self):
        	return self.nombre_unidad


class Material(models.Model):
    nombre_material         = models.CharField(max_length=200, verbose_name="Nombre", null=True)
    codigo_material         = models.CharField(max_length=50, verbose_name="Código de Repuesto")
    categoria_material      = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    unidad_material         = models.ForeignKey(Unidad, on_delete=models.CASCADE, verbose_name="Unidad", null=True)
    ubicacion_material      = models.CharField(max_length=200, verbose_name="Ubicación")
    stock_material          = models.IntegerField(default=0, verbose_name="Stock")
    marca                   = models.CharField(max_length=200, verbose_name="Marca", default="Sin marca")
    precio_unitario         = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="Precio unitario")
    creacion_material       = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_material   = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

    def __str__(self):
        texto_material  = "{1} | {0}"
        return texto_material.format(self.codigo_material, self.nombre_material)