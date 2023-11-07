from django import forms
from .models import Paciente, Medico, VisitaMedica


class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = Paciente

        fields = [
            'nombre',
            'dpi',
            'fecha_de_nacimiento',
            'direccion',
            'razon_de_visita',
            'receta_medica',
            'numero_telefonico',
        ]

        labels = {
            'nombre': 'Nombre completo',
            'dpi': 'Número de DPI',
            'fecha_de_nacimiento': 'Fecha de nacimiento',
            'direccion': 'Dirección',
            'razon_de_visita': 'Razón de visita',
            'receta_medica': 'Receta médica',
            'numero_telefonico': 'Número telefónico'
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'dpi': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su numero de DPI'
                }
            ),
            'fecha_de_nacimiento': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su dirección residencial'
                }
            ),
            'razon_de_visita': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su razón de visita'
                }
            ),
            'receta_medica': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su receta medica'
                }
            ),
            'numero_telefonico': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su número  telefónico'
                }
            ),
        }

    def clean_dpi(self):
        dpi = self.cleaned_data.get('dpi')
        if Paciente.objects.filter(dpi=dpi).exists():
            raise forms.ValidationError('Ya existe un paciente con este DPI.')
        return dpi


class FormularioMedico(forms.ModelForm):
    class Meta:
        model = Medico

        fields = [
            'nombre',
            'numero_colegiado',
            'especialidad',
            'diagnostico',
        ]

        labels = {
            'nombre': 'Nombre completo',
            'numero_colegiado': 'Número de colegiado',
            'especialidad': 'Especialidad',
            'diagnostico': 'Diagnostico',
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre'
                }
            ),
            'numero_colegiado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su numero de colegiado'
                }
            ),
            'especialidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su especialidad',
                }
            ),
            'diagnostico': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el diagnostico',
                }
            )
        }

    def clean_numero_colegiado(self):
        numero_colegiado = self.cleaned_data.get('numero_colegiado')
        if Medico.objects.filter(numero_colegiado=numero_colegiado).exists():
            raise forms.ValidationError("El número de colegiado ya existe. Debe ser único.")
        return numero_colegiado

class VisitaMedicaForm(forms.ModelForm):
    class Meta:
        model = VisitaMedica
        fields = ['medico', 'paciente', ]

        labels = {
            'medico': 'Médico',
            'paciente': 'Paciente',
        }