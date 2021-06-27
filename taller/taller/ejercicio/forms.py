from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from ejercicio.models import Edificio, Departamento

class FormEdificio(ModelForm):
      class Meta: 
            model = Edificio
            fields = ['nombre', 'dirreccion', 'ciudad', 'tipo']
            labels = {
                  'nombre': _('Ingrese el nombre'),
                  'dirreccion': _('Ingrese la dirrección'),
                  'ciudad': _('Ingrese la ciudad'),
                  'tipo': _('Ingrese el tipo de edificio'),
            }
      
      def clean_ciudad(self):
            valor = self.cleaned_data['ciudad']
            if valor[0] == "L" :
                  raise forms.ValidationError("El nombre de la ciudad no puede empezar con L")
            return valor

class FormDepartamento(ModelForm):
      class Meta: 
            model = Departamento
            fields = ['nombre_propietario', 'costo', 'cantidad_cuartos', 'edificio']
            labels = {
                  'nombre_propietario': _('Ingrese el nombre del propietario'),
                  'costo': _('Ingrese el costo del departamento'),
                  'cantidad_cuartos': _('Ingrese la cantidad de cuartos'),
                  'edificio': _('Ingrese el eficio al que pertenece'),
            }
            
      def clean_costo(self):
            valor = self.cleaned_data['costo']
            if float(valor) > 100000:
                  raise forms.ValidationError("El costo  no puede superar los $100 mil")
            return valor
      
      def clean_cantidad_cuartos(self):
            valor = self.cleaned_data['cantidad_cuartos']
            if int(valor) == 0  or int(valor) > 7:
                  raise forms.ValidationError("La cantidad no puede ser 0 ni mayor a 7")
            return valor

      def clean_nombre_propietario(self):
            valor = self.cleaned_data['nombre_propietario']
            num_palabras = len(valor.split())

            if num_palabras < 3:
                  raise forms.ValidationError("Ingrese el nombre completo por favor")
            return valor
            
            
            
class FormDepartamentoEdificio(ModelForm):
      def __init__(self, edificio, *args, **kwargs):
            super(FormDepartamentoEdificio, self).__init__(*args, **kwargs)
            self.initial['edificio'] = edificio
            self.fields["edificio"].widget = forms.widgets.HiddenInput()

      class Meta:
            model = Departamento
            fields = ['nombre_propietario', 'costo', 'cantidad_cuartos', 'edificio']
      
      def clean_costo(self):
            valor = self.cleaned_data['costo']
            if float(valor) > 100000:
                  raise forms.ValidationError("El costo  no puede superar los $100 mil")
            return valor
      
      def clean_cantidad_cuartos(self):
            valor = self.cleaned_data['cantidad_cuartos']
            if int(valor) == 0  or int(valor) > 7:
                  raise forms.ValidationError("La cantidad no puede ser 0 ni mayor a 7")
            return valor

      def clean_nombre_propietario(self):
            valor = self.cleaned_data['nombre_propietario']
            num_palabras = len(valor.split())

            if num_palabras < 3:
                  raise forms.ValidationError("Ingrese el nombre completo por favor")
            return valor
