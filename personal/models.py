from django.db import models
from django.contrib.auth.models import User
from trabajos.models import Trabajo

class Especialidad(models.Model):
    descripcion=models.CharField(max_length=155)
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
      return self.nombre

class Puesto(models.Model):
    descripcion=models.CharField(max_length=155)
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
      return self.nombre

class Privilegio(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
      return self.nombre

class Personal(models.Model):
    user=models.OneToOneField(User, unique=True)
    direccion=models.CharField(max_length=75, blank=True)
    fechaIngreso=models.DateField(auto_now=False, auto_now_add=False, blank=True)
    foto=models.CharField(max_length=255, blank=True)
    id=models.AutoField(primary_key=True)
    nss=models.CharField(max_length=16, blank=True)
    rfc=models.CharField(max_length=13, blank=True)
    telefono=models.CharField(max_length=15, blank=True)
    telefonoMovil=models.CharField(max_length=15, blank=True)
    trabajos=models.ManyToManyField(Trabajo, blank=True)
    especialidades=models.ManyToManyField(Especialidad, blank=True)
    puestos=models.ManyToManyField(Puesto, blank=True)
    privilegios=models.ManyToManyField(Privilegio, blank=True)

    def __unicode__(self):
      return self.user
