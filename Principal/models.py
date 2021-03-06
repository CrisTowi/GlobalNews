from django.db import models
from managers import UsuarioManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here
class Usuario(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(max_length=25, unique=True, db_index=True)
	nombre = models.CharField(max_length=45)
	ap_paterno = models.CharField(max_length=45)
	ap_materno = models.CharField(max_length=45)
	correo = models.CharField(max_length=45)
	foto = models.ImageField(upload_to = 'usuarios', null = True, blank = True)
	estado = models.CharField(max_length=45)

	activo = models.BooleanField(default=True, help_text='Activa un usuario para poder usar el sistema')
	administrador = models.BooleanField(default=False, help_text='Que usuarios se les permite entrar al administrador')
	
	objects = UsuarioManager()
	USERNAME_FIELD = 'username'
	
	def get_full_name(self):
		return self.username + ' ' + self.perfil

	def get_short_name(self):
		return self.username

	def __unicode__(self):
		return self.username

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.administrador

	@property
	def is_active(self):
		return self.activo

class Seccion(models.Model):
	nombre = models.CharField(max_length=45)

	def __unicode__(self):
		return self.nombre


class Subseccion(models.Model):
	seccion = models.ForeignKey(Seccion, related_name='seccion_subseccion')

	nombre = models.CharField(max_length=45)
	tiempo_aparicion = models.DateField()

	def __unicode__(self):
		return self.nombre

class Nota(models.Model):
	usuario = models.ForeignKey(Usuario, related_name='usuario_nota')
	subseccion = models.ForeignKey(Subseccion, related_name='subseccion_nota')

	titulo = models.CharField(max_length=45)
	descripcion = models.CharField(max_length=200)
	imagen = models.ImageField(blank=True, null=True, upload_to='notas')
	facha = models.DateTimeField(auto_now_add=True)
	longitud = models.IntegerField()
	latitud = models.IntegerField()
	likes = models.IntegerField(default=0)
	privacidad = models.BooleanField(default=True)

	def __unicode__(self):
		return self.descripcion

class ReporteNota(models.Model):
	usuario = models.ForeignKey(Usuario, related_name='usuario_reportenota')
	nota = models.ForeignKey(Nota, related_name='nota_reportenota')

	tipo = models.CharField(max_length=45)
	fecha = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario) + ' ' + str(self.nota)

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, related_name='usuario_comentario')
	nota = models.ForeignKey(Nota, related_name='nota_comentario')

	contenido = models.CharField(max_length=45)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.contenido

class ReporteUsuario(models.Model):
	usuario_reportado = models.ForeignKey(Usuario, related_name='usuario_reportado')
	usuario_reportador = models.ForeignKey(Usuario, related_name='usuario_reportador')

	tipo = models.CharField(max_length=45)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario_reportado) + ' ' + str(self.usuario_reportador)

class MensajeDirecto(models.Model):
	usuario_remitente = models.ForeignKey(Usuario, related_name='usuario_remitente')
	usuario_destinatario = models.ForeignKey(Usuario, related_name='usuario_destinatario')	

	contenido = models.CharField(max_length=50)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario_remitente) + ' ' + str(self.usuario_destinatario)

class UsuarioSigueUsuario(models.Model):
	usuario_seguido = models.ForeignKey(Usuario, related_name='usuario_seguido')
	usuario_seguidor = models.ForeignKey(Usuario, related_name='usuario_seguidor')

	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario_seguido) + ' ' + str(self.usuario_seguidor)

class UsuarioSigueSeccion(models.Model):
	usuario = models.ForeignKey(Usuario, related_name='usuario_sigueseccion')
	seccion = models.ForeignKey(Seccion, related_name='seccion_seguidausuario')

	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.usuario) + ' ' + str(self.seccion)
