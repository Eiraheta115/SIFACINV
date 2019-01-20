from django import forms
from .models import *
from functools import partial

class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ('idcliente', 'codigocli', 'registro', 'telefono', 'email', 'nombre', 'direccion', 'dui', 'saldo')

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ('idproveedor', 'codigoprov', 'registro', 'telefono', 'email', 'nombre', 'direccion', 'dui', 'saldo')
from .models import *

class newBodegaForm(forms.ModelForm):
    class Meta:
        model = Bodegas
        fields = [
            'nombre',
            'descripcion',
        ]

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())
