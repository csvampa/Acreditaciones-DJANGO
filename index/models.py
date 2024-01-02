from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
# from datetime import datetime, timedelta


class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField() #default=datetime.now()
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, limit_choices_to={'is_active': True}, related_name='eventos') 

    def __str__(self):
        return self.nombre
    
    def fechaHastaPredeterminada(self):
        return self.fechaFin 

ACCESO_CHOICES = [
        ('', 'Seleccionar...'),
        ('expositores', 'Expositores'),
        ('tecnica', 'Técnica'),
        ('trabajadores', 'Trabajadores'),
        ('allAccess', 'All Access'),
        ('armado', 'Armado'),
        ('desarme', 'Desarme'),
    ]

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cuit = models.IntegerField(blank=True, null=True)
    contacto = models.CharField(max_length=50, blank=True, null=True)
    acceso = models.CharField(max_length=20, choices= ACCESO_CHOICES, default='', blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    dni = models.IntegerField()
    nombreyapellido = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    acceso = models.CharField(max_length=20, choices= ACCESO_CHOICES, default='')
    asistencia = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=200, blank=True)
    fechaHastaSeguro = models.DateField(null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
       
    def save(self, *args, **kwargs):
        if not self.fechaHastaSeguro:
            self.evento = Evento.objects.get(pk=self.evento_id)
            self.fechaHastaSeguro = self.evento.fechaFin
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.nombre_y_apellido
    
    
    class Meta:
        unique_together = ('dni', 'evento')

class Seguro(models.Model):
    tipo = models.CharField(max_length=100)
    poliza = models.IntegerField(blank=True, null=True)
    montos = models.BooleanField()
    clausulas = models.BooleanField()
    fechaDesde = models.DateField()
    fechaHasta = models.DateField()
    tomador = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)