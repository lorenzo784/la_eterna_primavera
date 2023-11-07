from django.urls import path
from . import views

app_name = 'pagina'

urlpatterns = [
    path('', views.home, name='inicio'),
    path('historia', views.historia, name='historia'),
    path('contacto', views.contacto, name='contacto'),
    path('formularios', views.formulario, name='formularios'),
    path('paciente/crear', views.PacienteCreateView.as_view(), name='paciente-crear'),
    path('paciente', views.PacienteListView.as_view(), name='paciente-listado'),
    path('paciente/actualizar/<int:pk>', views.PacienteUpdateView.as_view(), name='paciente-actualizar'),
    path('paciente/borrar/<int:pk>', views.PacienteDeleteView.as_view(), name='paciente-borrar'),
    path('medico/crear', views.MedicoCreateView.as_view(), name='medico-crear'),
    path('medico', views.MedicoListView.as_view(), name='medico-listado'),
    path('medico/actualizar/<int:pk>', views.MedicoUpdateView.as_view(), name='medico-actualizar'),
    path('medico/borrar/<int:pk>', views.MedicoDeleteView.as_view(), name='medico-borrar'),
    path('visita/', views.crear_visita_medica, name='visita'),
    path('visita/listado/', views.listar_visitas_medicas, name='visita-listado'),
    path('visita/borrar/<int:pk>', views.EliminarVisitaMedica.as_view(), name='visita-borrar'),
]
