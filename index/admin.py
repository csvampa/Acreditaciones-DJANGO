from django.contrib import admin
from .models import Empresa, Evento, Persona, Seguro

admin.site.register(Empresa)
admin.site.register(Evento)
admin.site.register(Persona)
admin.site.register(Seguro)