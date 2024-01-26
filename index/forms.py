from django import forms
from .models import Persona
# from dal import autocomplete

class CargaIndividualForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'fechaHastaSeguro': forms.DateInput(attrs={'type': 'date'}),
            'empresa': forms.TextInput()
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