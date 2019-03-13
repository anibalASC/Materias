from django.db import models

# Create your models here.

class Materia(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=150) 

class Maestro(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=250)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)

class Alumno(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    maestro = models.ForeignKey(Maestro, on_delete = models.CASCADE)
