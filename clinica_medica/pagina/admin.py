from django.contrib import admin
from . import models


@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('name',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('name',)
