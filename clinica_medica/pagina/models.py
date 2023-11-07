from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=128)
    numero_colegiado = models.CharField(max_length=64)
    especialidad = models.CharField(max_length=64)
    diagnostico = models.CharField(max_length=128)

class Paciente(models.Model):
    nombre = models.CharField(max_length=128)
    dpi = models.CharField(max_length=64)
    foto = models.ImageField()
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=128)
    razon_de_visita = models.CharField(max_length=128)
    receta_medica = models.CharField(max_length=128)
    numero_telefonico = models.CharField(max_length=64)


