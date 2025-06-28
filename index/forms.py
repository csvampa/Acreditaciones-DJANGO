from django import forms
from .models import *
# from dal import autocomplete

class CargaIndividualForm(forms.ModelForm):
    empresa = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'empresa-input',
            'list': 'empresas-sugeridas',  # Conectado al <datalist>
            'placeholder': 'Escribí o seleccioná una empresa'
        })
    )
    class Meta:
        model = Persona
        fields = '__all__'
        exclude = ['empresa']
        labels = {
            'nombreyapellido': 'Nombre y Apellido',
            'dni': 'DNI',
            'fechaHastaSeguro': 'Vigencia del Seguro',
            'acceso': 'Tipo de Acceso',
            'asistencia': 'Asistencia',
            'observaciones': 'Observaciones Adicionales',
        }
        widgets = { 
            'fechaHastaSeguro': forms.DateInput(attrs={'type': 'date'}),
            #'empresa': forms.ModelChoiceField(required=False, queryset=Empresa.objects.all() )
            # 'empresa': autocomplete.ModelSelect2(url='empresa-autocomplete'),
        }

    def __init__(self, *args, evento=None, persona_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.evento = evento
        self.persona_id = persona_id

        self.existing_empresas = Empresa.objects.values_list('nombre', flat=True)

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if Persona.objects.filter(dni=dni, evento=self.evento).exclude(pk=self.persona_id).exists():
            raise forms.ValidationError(f"El DNI {dni} ya está registrado para este evento.")
        return dni
    
    def clean_empresa(self):
        nombre = self.cleaned_data.get('empresa')
        return nombre.strip() if nombre else None
    
class CargaMasivaForm(forms.Form):
    archivo_excel = forms.FileField(label='Suba un archivo Excel.')
    fechaHastaSeguro = forms.DateField(label='Vencimiento del Seguro')

class ActualizarDatos(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['asistencia']
        # 'dni', 'nombre_y_apellido', 'empresa', 'acceso', 