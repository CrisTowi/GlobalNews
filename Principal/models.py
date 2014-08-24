from django.db import models

# Create your models here
class Seccion(models.Model):
	nombre = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombre

class Subseccion(models.Model):
	seccion = models.ForeignKey(Seccion)

	nombre = models.CharField(max_length=45)
	tiempo_aparicion = models.DateField()

	def __unicode__(self):
		return self.nombre

class Usuario(models.Model):
	nombre = models.CharField(max_length=45)
	ap_paterno = models.CharField(max_length=45)
	ap_materno = models.CharField(max_length=45)
	username = models.CharField(max_length=30)
	correo = models.CharField(max_length=45)
	contrasena = models.CharField(max_length=30)
	foto = models.ImageField(blank=True, null=True, upload_to='usuarios')
	estado = models.CharField(max_length=45)

	def __unicode__(self):
		return self.Username

class Nota(models.Model):
	usuario = models.ForeignKey(Usuario)
	subseccion = models.ForeignKey(Subseccion)

	titulo = models.CharField(max_length=45)
	descripcion = models.CharField(max_length=200)
	imagen = models.ImageField(blank=True, null=True, upload_to='notas')
	facha = models.DateTimeField(auto_now_add=True)
	longitud = models.IntegerField()
	latitud = models.IntegerField()
	likes = models.IntegerField(default=0)
	privacidad = models.BooleanField()

	def __unicode__(self):
		return self.descripcion

class ReporteNota(models.Model):
	usuario = models.ForeignKey(Usuario)
	nota = models.ForeignKey(Nota)

	tipo = models.CharField(max_length=45)
	fecha = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario) + ' ' + str(self.nota)

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario)
	nota = models.ForeignKey(Nota)

	contenido = models.CharField(max_length=45)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.contenido

class ReporteUsuario(models.Model):
	usuario_reportado = models.ForeignKey(Usuario)
	usuario_reportador = models.ForeignKey(Usuario)

	tipo = models.CharField(max_length=45)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario_reportado) + ' ' + str(self.usuario_reportador)

class MensajeDirecto(models.Model):
	usuario_remitente = models.ForeignKey(Usuario)
	usuario_destinatario = models.ForeignKey(Usuario)	

	contenido = models.CharField(max_length=50)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario_remitente) + ' ' + str(self.usuario_destinatario)

class UsuarioSigueUsuario(models.Model):
	usuario_seguido = models.ForeignKey(Usuario)
	usuario_seguidor = models.ForeignKey(Usuario)

	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario_seguido) + ' ' + str(self.usuario_seguidor)

class UsuarioSigueSeccion(models.Model):
	usuario = models.ForeignKey(Usuario)
	seccion = models.ForeignKey(Seccion)

	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario) + ' ' + str(self.seccion)
