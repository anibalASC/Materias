# -*- encoding: utf-8 -*-
# from symbol import return_stmt

from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
# @python_2_unicode_compatible
class Materia(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=150) 
    
    

    def __str__(self):
        return self.nombre

class Maestro(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=250)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    maestro = models.ForeignKey(Maestro, on_delete = models.CASCADE)


    def __str__(self):
        return self.nombre