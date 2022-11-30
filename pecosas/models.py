from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.html import format_html
from django.utils.timezone import now

from materiales.models import Categoria, Material, Unidad
from solicitantes.models import Solicitante

####### Pecosa #######

class Pecosa(models.Model):
    matpecosa            = models.ManyToManyField(Material, through="PecosaMaterial")
    solicitante          = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    descripcion_pecosa   = models.TextField(verbose_name="Justificación")
    precio_total_pecosa  = models.DecimalField(max_digits=12, decimal_places=6, verbose_name="Precio total pecosa", null=True, blank=True)
    creacion_pecosa      = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    modificacion_pecosa  = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name = "pecosa"
        verbose_name_plural = "pecosas"
	  
    def __str__(self):
        	return self.descripcion_pecosa

# Calcular precio total de pecosa
@receiver(pre_save, sender=Pecosa)
def calcular_precio_total_pecosa(sender, instance, **kwargs):
    pecosa = instance.id
    obj = PecosaMaterial.objects.filter(pecosa_id = pecosa).aggregate(Sum('precio_total_material'))
    instance.precio_total_pecosa = obj['precio_total_material__sum']

class PecosaMaterial(models.Model):
    pecosa      = models.ForeignKey(Pecosa, on_delete=models.CASCADE) 
    material    = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad    = models.IntegerField(verbose_name="Cantidad")
    precio_total_material = models.DecimalField(max_digits=12, decimal_places=6, verbose_name="Precio total del material", null=True, blank=True)
    
    def __unicode__(self):
        return self.pecosa
    

def update_stock(sender, instance, **kwargs):
    instance.material.stock_material -= instance.cantidad
    instance.material.save()

# register the signal (post sinal - actualizar stock)
post_save.connect(update_stock, sender=PecosaMaterial, dispatch_uid="update_stock_count")

# Calcular precio total de cada material
@receiver(pre_save, sender=PecosaMaterial)
def calcular_precio_total_material(sender, instance, **kwargs):
    material = instance.material_id
    instance.precio_total_material = instance.material.precio_unitario * instance.cantidad

####### Entrada #######

class Entrada(models.Model):
    descripcion_entrada  = models.TextField(verbose_name='Descripción')
    matentrada           = models.ManyToManyField(Material, through="EntradaMaterial")
    creacion_entrada     = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Fecha de creación")
    modificacion_entrada = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
	  
    def __str__(self):
        	return self.descripcion_entrada

class EntradaMaterial(models.Model):
    entrada             = models.ForeignKey(Entrada, on_delete=models.CASCADE) 
    material            = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad_entrada    = models.IntegerField(verbose_name="Cantidad")
    
    def __unicode__(self):
        return self.entrada

def update_stock(sender, instance, **kwargs):
        instance.material.stock_material += instance.cantidad_entrada
        instance.material.save()

# register the signal
post_save.connect(update_stock, sender=EntradaMaterial, dispatch_uid="update_stock_count")


####### Mermas #######

class Merma(models.Model):
    descripcion_merma   = models.TextField(verbose_name='Descripción')
    matmerma            = models.ManyToManyField(Material, through="MermaMaterial")
    creacion_merma      = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Fecha de creación")
    modificacion_merma  = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    
    class Meta:
        verbose_name = "merma"
        verbose_name_plural = "mermas"
	  
    def __str__(self):
        	return self.descripcion_merma
    
class MermaMaterial(models.Model):
    merma           = models.ForeignKey(Merma, on_delete=models.CASCADE) 
    material        = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad_merma  = models.IntegerField(verbose_name="Cantidad")
    
    def __unicode__(self):
        return self.merma

def update_stock(sender, instance, **kwargs):
        instance.material.stock_material -= instance.cantidad_merma
        instance.material.save()

# register the signal
post_save.connect(update_stock, sender=MermaMaterial, dispatch_uid="update_stock_count")