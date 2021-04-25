from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    # Metadata
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.descripcion

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ["categoria"]

    def __str__(self):
        return self.descripcion

class Proforma(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=200)
    cedula = models.CharField(max_length=10)
    fecha = models.DateField()

    def calcular_subtotal(self):
        suma = sum([proD.importe for proD in Proforma_Detalle.objects.filter(proforma=self.id)])
        return suma
    subtotal = property(calcular_subtotal)

    def calcular_iva(self):
        return round(self.calcular_subtotal().__float__()*0.12,2)
    iva = property(calcular_iva)

    def calcular_total(self):
        return round(self.calcular_subtotal().__float__()+self.calcular_iva(),2)
    total = property(calcular_total)
    # Metadata
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)

class Proforma_Detalle(models.Model):
    # campos
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    proforma = models.ForeignKey(Proforma, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Servicio)
 
    def calcular_importe(self):
        return self.cantidad * self.servicio.get().precio
    importe = property(calcular_importe)

    def ver_precio(self):
        return self.servicio.get().precio
    precio = property(ver_precio)
    def ver_servicios(self):
        """
        Metodo que retorna los servicios que tenemos disponibles
        """
        return self.servicio.get().descripcion
    ver_servicios.short_descriptioons = 'Servicio'

    # Metadata
    class Meta:
        ordering = ["proforma"]

    def __str__(self):
        return str(self.id)