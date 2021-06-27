from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

from ejercicio.models import *
from ejercicio.forms import *

def index(request):
      edificios = Edificio.objects.all()
      informacion = {'edificios': edificios}
      return render(request, 'index.html', informacion)

def crear_edificio(request):
      if request.method=='POST':
            form = FormEdificio(request.POST)
            if form.is_valid():
                  form.save() 
                  return redirect(index)
      else:
            form = FormEdificio()
            
      titulo = "Añadir edificio"
      informacion = {'form':form, 'titulo':titulo}
      return render(request, 'edificios.html',  informacion)
      
def editar_edificio(request, id):
      edificio = Edificio.objects.get(pk=id)
      if request.method=='POST':
            form = FormEdificio(request.POST, instance=edificio)
            if form.is_valid():
                  form.save() 
                  return redirect(index)
      else:
            form = FormEdificio(instance=edificio)
            
      titulo = "Editar información del edificio"
      informacion = {'form':form, 'titulo':titulo}
      return render(request, 'edificios.html',  informacion)

def eliminar_edificio(request, id):
      Edificio.objects.get(pk=id).delete()
      return redirect(index)


def crear_departamento(request):
      if request.method=='POST':
            form = FormDepartamento(request.POST)
            if form.is_valid():
                  form.save() 
                  return redirect(index)
      else:
            form = FormDepartamento()
      
      titulo = "Añadir departamento"
      informacion = {'form':form, 'titulo':titulo}
      return render(request, 'departamentos.html',  informacion)
      
def editar_departamento(request, id):
      departamento = Departamento.objects.get(pk=id)
      if request.method=='POST':
            form = FormDepartamento(request.POST, instance=departamento)
            if form.is_valid():
                  form.save() 
                  return redirect(index)
      else:
            form = FormDepartamento(instance=departamento)
      
      titulo = "Editar información del departamento"
      informacion = {'form':form, 'titulo':titulo}
      return render(request, 'departamentos.html',  informacion)

def eliminar_departamento(request, id):
      Departamento.objects.get(pk=id).delete()
      return redirect(index)


def crear_departamento_edificio(request, id):
      edificio = Edificio.objects.get(pk=id)
      if request.method=='POST':
            form = FormDepartamentoEdificio(edificio, request.POST)
            if form.is_valid():
                  form.save()
                  return redirect(index)
      else:
            form = FormDepartamentoEdificio(edificio)
            
      titulo = "Añadir departamento al edificio"
      diccionario = {'form': form, 'edificio': edificio, 'titulo':titulo, 'valor':True}
      return render(request, 'departamentos.html', diccionario)