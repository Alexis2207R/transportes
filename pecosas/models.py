from django.db import models
from django.utils.timezone import now
from solicitantes.models import Solicitante
from materiales.models import Material

class Pecosa(models.Model):
    matpecosa            = models.ManyToManyField(Material, through="PecosaMaterial")
    solicitante          = models.ForeignKey(Solicitante, on_delete=models.CASCADE, null=True)
    descripcion_pecosa   = models.CharField(max_length=200, verbose_name="Descripcion")
    creacion_pecosa      = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_pecosa  = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "pecosa"
        verbose_name_plural = "pecosas"
	  
    def __str__(self):
        	return self.descripcion_pecosa

class PecosaMaterial(models.Model):
    pecosa      = models.ForeignKey(Pecosa, on_delete=models.CASCADE) 
    material    = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad    = models.IntegerField(default=1)