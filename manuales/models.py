from django.db import models

class CategoriaMan(models.Model):
	descripcion=models.CharField(max_length=255)

	def __unicode__(self):
		return self.descripcion

class Formato(models.Model):
	nombre = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombre

class Manual(models.Model):
    idioma=models.CharField(max_length=45)
    tags=models.CharField(max_length=255)
    titulo=models.CharField(max_length=155)
    ubucacion=models.CharField(max_length=55)
    CategoriaMan=models.ForeignKey(CategoriaMan)
    Formato=models.ForeignKey(Formato)
    
    def __unicode__(self):
      return self.titulo
