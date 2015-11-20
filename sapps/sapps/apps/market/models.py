from django.db import models

# Create your models here.
class Tipo(models.Model):
	nombre			= models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre

class Categoria(models.Model):
	nombre			= models.CharField(max_length = 100)
	descripcion		= models.TextField(max_length = 500)
	tipo 			= models.ForeignKey(Tipo)
	def __unicode__ (self):
		return self.nombre

class Plataforma(models.Model):
	nombre			= models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre

class Clasificacion(models.Model):
	nombre			= models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre

class Estado(models.Model):
	nombre			= models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre

class Regional(models.Model):
	nombre			= models.CharField(max_length = 100)
	def __unicode__ (self):
		return self.nombre

class Centro(models.Model):
	nombre			= models.CharField(max_length = 100)
	regional 		= models.ForeignKey(Regional)
	def __unicode__ (self):
		return self.nombre

tipos_usuaro=(
	('registrado','registrado'),
	('desarrollador','desarrollador'),
	)


class Usuario(models.Model):
	def url(self, filename):
		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre, str(filename))
		return ruta
	nombre			= models.CharField(max_length = 100)
	apellidos		= models.CharField(max_length = 100)
	telefono		= models.CharField(max_length = 30)
	imagen			= models.ImageField(upload_to = url, null = True, blank = True)
	regional 		= models.ForeignKey(Regional)
	tipo_usuario 	= models.CharField(choices = tipos_usuaro, max_length = 30) 			
	#user 			= models.OneToOneField(User)
	def __unicode__ (self):
		return self.nombre

class Aplicacion (models.Model):
	def url(self, filename):
		ruta = "MultimediaData/Producto/%s/%s"%(self.titulo, str(filename))
		return ruta

	titulo			= models.CharField(max_length = 100)
	descripcion		= models.TextField(max_length = 500)
	icono			= models.ImageField(upload_to = url, null = True, blank = True)
	imagen			= models.ImageField(upload_to = url, null = True, blank = True)
	video_url		= models.CharField(max_length = 100)
	web				= models.TextField(max_length = 500)
	apk		 		= models.FileField(upload_to = url, null = True, blank = True)
	categoria 		= models.ForeignKey(Categoria)
	clasificacion	= models.ForeignKey(Clasificacion)
	plataformas		= models.ManyToManyField(Plataforma, null = True, blank = True)
	estado			= models.ForeignKey(Estado)
	usuario			= models.ForeignKey(Usuario)

	def __unicode__ (self):
		return self.titulo



