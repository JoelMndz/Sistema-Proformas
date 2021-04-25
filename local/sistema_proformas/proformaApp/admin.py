from django.contrib import admin
from proformaApp.models import Servicio, Categoria, Proforma, Proforma_Detalle
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id","descripcion")

class ServicioAdmin(admin.ModelAdmin):
    list_display = ("id","descripcion","precio","categoria")

class ProformaDetalleAdmin(admin.ModelAdmin):
    list_display = ("id","proforma","cantidad", "ver_servicios","importe")

class ProformaAdmin(admin.ModelAdmin):
    list_display = ("id","cliente","cedula","fecha","subtotal","iva","total")

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Proforma, ProformaAdmin)
admin.site.register(Proforma_Detalle, ProformaDetalleAdmin)
