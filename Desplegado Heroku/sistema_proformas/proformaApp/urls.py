from django.urls import path
from proformaApp import views

urlpatterns = [
    path('', views.home),
    path('crear_proforma/', views.crear_proforma, name = 'crearProforma'),
    path('detalle_proforma1/', views.procesar_proforma, name = 'detalleProforma1'),
    path('detalle_proforma2/', views.detalle_proforma, name = 'detalleProforma2'),
    path('desplegar_proforma/', views.desplegar_proforma, name = 'desplegarProforma'),
]