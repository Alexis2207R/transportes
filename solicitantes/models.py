from django.db import models
from django.utils.timezone import now

class Solicitante(models.Model):
    nombre_solicitante        = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion_solicitante   = models.TextField(verbose_name="Descripcion")
    creacion_solicitante      = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_solicitante  = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "solicitante"
        verbose_name_plural = "solicitantes"
	  
    def __str__(self):
        	return self.nombre_solicitante