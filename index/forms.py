from django import forms
from .models import *
# from dal import autocomplete

class CargaIndividualForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),  # Aquí definimos el queryset para obtener las empresas
        required=False,  # Lo dejamos como no obligatorio por si el usuario quiere escribir una nueva empresa
        widget=forms.Select(attrs={'class': 'empresa-select'})
    )
    dni = forms.IntegerField(label='DNI')
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = { 
            'fechaHastaSeguro': forms.DateInput(attrs={'type': 'date'}),
            #'empresa': forms.ModelChoiceField(required=False, queryset=Empresa.objects.all() )
            # 'empresa': autocomplete.ModelSelect2(url='empresa-autocomplete'),
        }

class CargaMasivaForm(forms.Form):
    archivo_excel = forms.FileField(label='Suba un archivo Excel.')
    fechaHastaSeguro = forms.DateField(label='Vencimiento del Seguro')

class ActualizarDatos(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['asistencia']
        # 'dni', 'nombre_y_apellido', 'empresa', 'acceso', 