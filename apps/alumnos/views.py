from django.shortcuts import render
from .models import *
from .forms import MateriaForm

# Create your views here.

def home(request):
    return render(request,'index.html')

# funcion para crear una materia
def crearMateria(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MateriaForm()
    return render(request, 'templates/SistemaMaterias/crear_materia.html',{'form':form})

"""
# funcion para crear un maestro
def crearMaestro(request):
    if request.method == 'POST':
        form = MaestroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MaestroForm()
    return render(request, 'templates/SistemaMaterias/crear_maestro.html',{'form':form})

# funcion para crear alumno
def crearAlumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlumnoForm()
    return render(request, 'templates/SistemaMaterias/crear_alumno.html',{'form':form})

"""