from django.urls import path
from ejercicio.views import *

urlpatterns = [
      path('', index, name='index'), 
      path('anadir-edificio', crear_edificio, name='crear_edificio'),
      path('editar-edificio/<int:id>', editar_edificio, name='editar_edificio'),
      path('eliminar-edificio/<int:id>', eliminar_edificio, name='eliminar_edificio'),
      path('anadir-departamento', crear_departamento, name='crear_departamento'),
      path('editar-departamento/<int:id>', editar_departamento, name='editar_departamento'),
      path('eliminar-departamento/<int:id>', eliminar_departamento, name='eliminar_departamento'),
      path('anadir-departamento-edificio/<int:id>', crear_departamento_edificio, name='crear_departamento_edificio'),      
]