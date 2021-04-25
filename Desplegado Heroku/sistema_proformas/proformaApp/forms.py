from django import forms
from proformaApp.models import Proforma, Proforma_Detalle

class FormularioProforma(forms.ModelForm):
    class Meta:
        model = Proforma
        fields = '__all__'
        widgets = {'fecha': forms.DateInput(attrs={'type': 'date'})}
        
class FormularioProformaDetalle(forms.ModelForm):
    class Meta:
        model = Proforma_Detalle
        fields = '__all__'