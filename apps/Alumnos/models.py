# from xmlrpclib import DateTime

# from pip import models

from django.db import models


# Create your models here.
class Alumnos(models.Model):
    nombre = models.CharField(max_length=200, help_text = 'Nombre(s)')
    a_paterno = models.CharField(max_length=200, help_text = 'Apellido Paterno')
    a_materno =  models.CharField(max_lenght=200, help_text = 'Apellido Materno')
    f_nacimiento = models.DateTimeField(blank=True, null=True, help_text = 'Fecha de nacimiento')

    def __srt__(self):
        return self.titles