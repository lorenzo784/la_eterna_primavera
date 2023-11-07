from django.db import models

class Medico(models.Model):
    nombre = models.CharField(max_length=128)
    numero_colegiado = models.CharField(max_length=64)
    especialidad = models.CharField(max_length=64)
    diagnostico = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=128)
    dpi = models.CharField(max_length=64, unique=True)
    foto = models.ImageField()
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=128)
    razon_de_visita = models.CharField(max_length=128)
    receta_medica = models.CharField(max_length=128)
    numero_telefonico = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre

    

class VisitaMedica(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_visita = models.DateField(auto_now_add=True)