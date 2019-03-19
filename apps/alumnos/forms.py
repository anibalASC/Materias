from django import forms
from .models import Materia, Maestro, Alumno

class MateriaForm(forms.ModelForm):
    
    class Meta:
        model = Materia
        fields = [
            'nombre',
            ]

class MaestroForm(forms.ModelForm):
    
    class Meta:
        model = Maestro
        fields = [
            'nombre',
            'materia',
            ]

class AlumnoForm(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = [
            'nombre',
            'apellido',
            'edad',
            'maestro',
            ]
