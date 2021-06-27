from django.db import models

class Edificio(models.Model):
      tipos = (( 'Residencial', 'Residencial'), ('Comercial', 'Comercial' ))
      
      nombre = models.CharField(max_length=50)
      dirreccion = models.CharField(max_length=100)
      ciudad = models.CharField(max_length=30)
      tipo = models.CharField(max_length=20, choices=tipos )
      
      def obtener_cuartos_departamentos(self):
            valor = [x.cantidad_cuartos for x in self.departamentos.all()]
            valor = sum(valor)
            return valor
      
      def obtener_costo_departamentos(self):
            valor = [x.costo for x in self.departamentos.all()]
            valor = sum(valor)
            return valor

      def __str__(self):
            return "%s - %s - %s" % (self.nombre,
                  self.dirreccion,
                  self.tipo)
            
            
class Departamento(models.Model):
      nombre_propietario = models.CharField(max_length=100)
      costo = models.FloatField()
      cantidad_cuartos = models.IntegerField()
      edificio =models.ForeignKey(Edificio(), on_delete=models.CASCADE,
            related_name="departamentos")

      def __str__(self):
            return "%s %s %s" % (  self.edificio,
                  self.costo,
                  self.cantidad_cuartos)