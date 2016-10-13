from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	class Meta:
		db_table = 'auth_user'

	TIPO_USUARIO = (
		("A", "Administrador"),
		("S", "Sicologo"),
		("E", "Estudiante"),
	)

	TIPO_DE_DOCUMENTO = (
		("C.C", "Cedula de ciudadania"),
		("T.I", "Tarjeta de identidad"),
	)

	TIPO_DE_GENERO = (
		("M", "Masculino"),
		("F", "Femenino")
	)

	tipo_usuario = models.CharField(max_length=15, choices=TIPO_USUARIO)
	tipo_genero = models.CharField(max_length=10, choices=TIPO_DE_GENERO)
	tipo_documento = models.CharField(max_length=20, choices=TIPO_DE_DOCUMENTO)
	documento = models.CharField(max_length=10)
	direccion = models.CharField(max_length=20)
	telefono = models.CharField(max_length = 12)
	fecha_nacimiento = models.DateField(null=True, blank=True)

class Administrador(Usuario):
	class Meta:
		verbose_name = "Administrador"
	

class Sicologo(Usuario):
	class Meta:
		verbose_name = "Sicologo"
	

class Estudiante(Usuario):
	class Meta:
		verbose_name = "Estudiante"
	

class Institucion(models.Model):
	nit = models.CharField(max_length=15)
	nombre = models.CharField(max_length=100)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=12)
	ciudad = models.CharField(max_length=20)
	sitio_web = models.URLField(max_length=50)

	def __str__(self):
		return self.nit + ' ' + self.nombre

class Grupo(models.Model):
	institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=10)
	grado = models.CharField(max_length=10)
	jornada = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre