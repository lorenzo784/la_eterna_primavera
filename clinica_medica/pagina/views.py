from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Paciente, Medico, VisitaMedica
from .forms import FormularioPaciente, FormularioMedico, VisitaMedicaForm, FormularioPacienteEditar, FormularioMedicoEditar
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


def home(request):
    return render(request, 'pagina/inicio.html')

def historia(request):
    return render(request, 'pagina/historia.html')

def contacto(request):
    return render(request, 'pagina/contacto.html')

def formulario(request):
    return render(request, 'pagina/formularios.html')

class PacienteListView(ListView):
    model = Paciente
    template_name = 'pagina/paciente/lista.html'

@method_decorator(login_required, name='dispatch')
class PacienteCreateView(CreateView):
    model = Paciente
    form_class = FormularioPaciente
    template_name = 'pagina/paciente/crear.html'
    success_url = reverse_lazy('pagina:paciente-listado')

@method_decorator(login_required, name='dispatch')
class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = FormularioPacienteEditar
    template_name = 'pagina/paciente/actualizar.html'
    success_url = reverse_lazy('pagina:paciente-listado')

@method_decorator(login_required, name='dispatch')
class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'pagina/paciente/eliminar.html'
    success_url = reverse_lazy('pagina:paciente-listado')

class MedicoListView(ListView):
    model = Medico
    template_name = 'pagina/medico/lista.html'

@method_decorator(login_required, name='dispatch')
class MedicoCreateView(CreateView):
    model = Medico
    form_class = FormularioMedico
    template_name = 'pagina/medico/crear.html'
    success_url = reverse_lazy('pagina:medico-listado')

@method_decorator(login_required, name='dispatch')
class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = FormularioMedicoEditar
    template_name = 'pagina/medico/actualizar.html'
    success_url = reverse_lazy('pagina:medico-listado')

@method_decorator(login_required, name='dispatch')
class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'pagina/medico/eliminar.html'
    success_url = reverse_lazy('pagina:medico-listado')

@login_required
def crear_visita_medica(request):
    if request.method == 'POST':
        form = VisitaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina:visita-listado')
    else:
        form = VisitaMedicaForm()
    
    return render(request, 'pagina/visita_medica.html', {'form': form})

def listar_visitas_medicas(request):
    visitas = VisitaMedica.objects.all()
    return render(request, 'pagina/visita_listado.html', {'visitas': visitas})

@method_decorator(login_required, name='dispatch')
class EliminarVisitaMedica(DeleteView):
    model = VisitaMedica
    template_name = 'pagina/visita_borrar.html'
    success_url = reverse_lazy('pagina:visita-listado')