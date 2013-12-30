from django.db import models

class Problema(models.Model):
    nombrecorto=models.CharField(max_length=45)
    descripcion=models.CharField(max_length=255)
    dispositivo=models.CharField(max_length=155)
    id=models.AutoField(primary_key=True)
    marca=models.CharField(max_length=55)
    modelo=models.CharField(max_length=55)
    solucion=models.CharField(max_length=255)
    
    def __unicode__(self):
      return self.nombrecorto