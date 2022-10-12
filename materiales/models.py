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

class Material(models.Model):
    nombre_material         = models.CharField(max_length=200, verbose_name="Nombre")
    categoria_material      = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    stock_material          = models.IntegerField(verbose_name="stock")
    creacion_material       = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_material   = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

    def __str__(self):
        	return self.nombre_material