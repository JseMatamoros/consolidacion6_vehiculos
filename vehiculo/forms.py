from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        exclude = ['condicion_precio']
        fields = '__all__' 
