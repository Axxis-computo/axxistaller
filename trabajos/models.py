from django.db import models
from problemas.models import Problema

class Accion(models.Model):
    descripcion=models.CharField(max_length=255)
    fechaHora=models.DateTimeField(auto_now=False, auto_now_add=False)
    id=models.AutoField(primary_key=True)
 
    def __unicode__(self):
      return self.descripcion

class estadoTrabajo(models.Model):
    descripcion=models.CharField(max_length=55)
    id=models.AutoField(primary_key=True)
  
    def __unicode__(self):
      return self.descripcion

class Trabajo(models.Model):
    costoEstimado=models.DecimalField(max_digits=8, decimal_places=2)
    costoFinal=models.DecimalField(max_digits=8, decimal_places=2)
    descripcion=models.CharField(max_length=255)
    fechaEntrega=models.DateField(auto_now=False, auto_now_add=False)
    fechaIngreso=models.DateField(auto_now=False, auto_now_add=False)
    id=models.AutoField(primary_key=True)
    problemas=models.ManyToManyField(Problema)
    acciones=models.ManyToManyField(Accion)
    estadoTrabajo=models.ForeignKey(estadoTrabajo)

    def __unicode__(self):
      return self.descripcion