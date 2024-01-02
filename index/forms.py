from django import forms
from .models import ACCESO_CHOICES, Persona

class CargaIndividualForm(forms.Form):
    dni = forms.IntegerField(label='DNI')
    nombreyapellido = forms.CharField(label='Nombre y Apellido', max_length=200)
    empresa = forms.CharField(label='Empresa', max_length=100)
    acceso = forms.ChoiceField(label='Acceso', choices=ACCESO_CHOICES)
    observaciones = forms.CharField(label='Observaciones', max_length=500, required=False)
    fechaHastaSeguro = forms.DateField(label='Vencimiento del Seguro', required=False)
    asistencia = forms.BooleanField(label='Asistencia', required=False)

class CargaMasivaForm(forms.Form):
    archivo_excel = forms.FileField(label='Suba un archivo Excel.')
    fechaHastaSeguro = forms.DateField(label='Vencimiento del Seguro')

class ActualizarDatos(forms.Form):
    class Meta:
        model = Persona
        fields = ['dni', 'nombre_y_apellido', 'empresa', 'acceso', 'asistencia']