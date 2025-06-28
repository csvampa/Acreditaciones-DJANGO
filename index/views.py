from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, Empresa, Evento
from .forms import CargaIndividualForm, CargaMasivaForm, ActualizarDatos
import pandas as pd
from datetime import datetime
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View
from django.db.models import Q

class Eventos(View):
    def __init__(self,) -> None:
        pass
    
    def get(self, request):
        user=request.user
        if user.is_superuser:
            eventos = Evento.objects.all()
            fecha_actual = datetime.now()
            return render(request, 'eventos.html', {'eventos': eventos, 'fecha_actual': fecha_actual})
        else:
            return redirect('login')
        
class Personas(View):
    def __init__(self) -> None:
        pass
    def dispatch(self, request, *args, **kwargs):
        # Obtén los valores de evento_id y evento_nombre de los kwargs
        self.evento_id = kwargs.get('evento_id')
        self.evento_nombre = kwargs.get('evento_nombre')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, evento_id, evento_nombre):
        evento = Evento.objects.get(pk=evento_id)
        personas = Persona.objects.filter(evento=evento)
        fecha_actual = datetime.now()
        return render(request, 'index.html', {'personas': personas, 'fecha_actual': fecha_actual, 'nombre_evento':evento_nombre, 'id_evento':evento_id})
    #  POST PARA ASISTENCIA
    def post(self, request, evento_nombre, evento_id):
        persona_id = request.POST.get('persona_id')
        persona = get_object_or_404(Persona, pk=persona_id)
        if request.method == 'POST':
            form = ActualizarDatos(request.POST, instance=persona)
            if form.is_valid():
                form.save()
        return redirect('db_evento', evento_nombre=evento_nombre, evento_id=evento_id)
    '''def put(self, request,evento_id):
        evento = Evento.objects.get(pk=evento_id)
        form = CargaIndividualForm()
        return render(request, 'cargaIndividual.html', {'form': form, 'evento': evento})'''
            
def cargaIndividual(request, evento_id, evento_nombre, persona_id=None):
    evento = get_object_or_404(Evento, pk=evento_id)
    persona_existente = None
    if persona_id:
        persona_existente = get_object_or_404(Persona, pk=persona_id, evento=evento)
    if request.method == 'POST':
        form = CargaIndividualForm(request.POST, instance=persona_existente, evento=evento, persona_id=persona_id)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.evento = evento
            # Crear empresa si es necesario
            empresa_nombre = form.cleaned_data.get('empresa')
            if empresa_nombre:
                empresa_obj, _ = Empresa.objects.get_or_create(nombre=empresa_nombre)
                persona.empresa = empresa_obj
            else:
                persona.empresa = None           
            persona.save()
            messages.success(request, f'Datos de la persona con DNI {persona.dni} guardados correctamente.')
            return redirect(reverse('db_evento', args=[evento_id, evento_nombre]))
        else:
            messages.error(request, 'Revisá los errores en el formulario.')
    else:
        form = CargaIndividualForm(instance=persona_existente, evento=evento, persona_id=persona_id)
    return render(request, 'cargaIndividual.html', {'form': form, 'evento': evento})

def cargaMasiva(request, evento_id, evento_nombre):
    evento = Evento.objects.get(pk=evento_id)
    if request.method == 'GET':
        return render(request, 'cargaMasiva.html', {'form': CargaMasivaForm()})
    else:
        archivo = request.FILES['archivo_excel']
        if archivo.name.endswith('.xls') or archivo.name.endswith('.xlsx'):
            df = pd.read_excel(archivo) # Lee el archivo Excel usando pandas
            dni_existentes = list(Persona.objects.values_list('dni', flat=True))
            for _, row in df.iterrows():
                dni = row['DNI']
                if dni in dni_existentes:
                    previous_url = request.META.get('HTTP_REFERER') 
                    messages.error(request, f'El DNI {dni} ya existe en la base de datos.')
                    return render(request,'error.html',{'previous_url': previous_url})  # Redirige a una vista de error
                else:
                    empresa_nombre = row['EMPRESA']
                    empresa, _ = Empresa.objects.get_or_create(nombre=empresa_nombre)
                    nombreyapellido=row['NOMBRE Y APELLIDO']
                    acceso=row['ACCESO']
                    observaciones=row.get('OBSERVACIONES', '')
                    fechaHastaSeguro=row.get('FECHA HASTA', None)
                    try:
                        fechaHastaSeguro = datetime.fromisoformat(fechaHastaSeguro)
                    except (ValueError, TypeError):
                        fechaHastaSeguro = None 

                    observaciones = observaciones if observaciones else None
                    fechaHastaSeguro = fechaHastaSeguro if fechaHastaSeguro  else None

                    Persona.objects.create(
                    dni=dni,
                    nombreyapellido=nombreyapellido,
                    empresa=empresa,
                    acceso=acceso,
                    asistencia=False,
                    observaciones=observaciones,
                    fechaHastaSeguro=fechaHastaSeguro,
                    evento=evento,
                    )
            evento_nombre = evento.nombre
            url = reverse('db_evento', args=[evento_id, evento_nombre])
            return redirect(url)
        else:
            return render(request, 'error.html', {'mensaje': 'El archivo no es un archivo Excel válido.'})

def error_view(request):
    return render(request, 'error.html')