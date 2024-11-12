from django.contrib import admin
from .models import Paciente, Modelo, Zona, Examen, Prediccion

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Modelo)
admin.site.register(Zona)
admin.site.register(Examen)
admin.site.register(Prediccion)