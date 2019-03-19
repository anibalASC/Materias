from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="index"),
    path("crear_materia/",crearMateria,name="crear_materia"),
]