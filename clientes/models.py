from django.db import models
from trabajos.models import Trabajo

class Cliente(models.Model):
    aMaterno=models.CharField(max_length=75)
    aPaterno=models.CharField(max_length=75)
    correo=models.CharField(max_length=50)
    direccion=models.CharField(max_length=75)
    fechaIngreso=models.DateField(auto_now=False, auto_now_add=False)
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    rfc=models.CharField(max_length=13)
    telefono=models.CharField(max_length=15)
    telefonoMovil=models.CharField(max_length=15)
    trabajos=models.ManyToManyField(Trabajo, blank=True)

    def __unicode__(self):
      return self.nombre+' '+self.aPaterno+' '+self.aMaterno
