from django.contrib import admin
from . import models


@admin.register(models.Usuario)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)