from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
from proformaApp.forms import FormularioProforma, FormularioProformaDetalle
from proformaApp.models import Proforma, Proforma_Detalle

id_proforma = 0
# Vista principal
def home(request):
    return render(request,"home.html")

# Vista para pedir datos de la proforma
def crear_proforma(request):
    proforma = FormularioProforma()
    return render(request,"crearProforma.html",{'form': proforma})

def procesar_proforma(request):
    proforma = FormularioProforma(request.POST)
    if proforma.is_valid():
        proforma.save()
        global id_proforma
        id_proforma = [p.id for p in Proforma.objects.filter(cliente=request.POST['cliente'], cedula=request.POST['cedula'])].pop()
    proformaDetalle = FormularioProformaDetalle()
    return render(request,"detalleProforma.html",{'form':proformaDetalle,'id':id_proforma})   
# Vista crear proforma
def detalle_proforma(request):
    proformaDetalle = FormularioProformaDetalle(request.POST)
    if proformaDetalle.is_valid():
        proformaDetalle.save()
    proformaDetalle = FormularioProformaDetalle()
    return render(request,"detalleProforma.html",{'form':proformaDetalle,'id':id_proforma,'mensaje':'ok'})
  
# Vista para desplegar proforma
def desplegar_proforma(request):
    proforma = [p for p in Proforma.objects.filter(id=id_proforma)]
    detalles = [d for d in Proforma_Detalle.objects.filter(proforma=id_proforma)]
    return render(request,"desplegarProforma.html",{'proforma':proforma,'detalles':detalles})