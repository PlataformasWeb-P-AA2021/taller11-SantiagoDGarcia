from django.contrib import admin
from ejercicio.models import Edificio, Departamento

class EdificiosAdministracion(admin.ModelAdmin):
    list_display = ('nombre', 'dirreccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'ciudad')
    
class DepartamentosAdministracion(admin.ModelAdmin):
    list_display = ('nombre_propietario', 'costo', 'cantidad_cuartos', 'edificio')
    search_fields = ('nombre_propietario', 'edificio')
    
admin.site.register(Edificio, EdificiosAdministracion)
admin.site.register(Departamento, DepartamentosAdministracion)
