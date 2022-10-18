from django.db import models
from django.utils.timezone import now
from .choices import sexos

class Area(models.Model):
    nombre_area         = models.CharField(max_length=200, verbose_name="Nombre")
    creacion_area       = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_area   = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
	  
    def __str__(self):
        	return self.nombre_area

class Solicitante(models.Model):
    nombre_solicitante        = models.CharField(max_length=200, verbose_name="Nombre")
    area                      = models.ForeignKey(Area, on_delete=models.CASCADE)
    sexo_solicitante          = models.CharField(max_length=1, choices=sexos, default='M', verbose_name="Sexo")
    telefono_solicitante      = models.CharField(max_length=13, verbose_name="telefono")
    creacion_solicitante      = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_solicitante  = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "solicitante"
        verbose_name_plural = "solicitantes"
	  
    def __str__(self):
        	return self.nombre_solicitante