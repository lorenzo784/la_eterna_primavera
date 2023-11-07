from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usuario'

urlpatterns = [
    path('iniciar/', views.user_login, name='iniciar'),
    path('registrar/', views.user_register, name='registrar'),
    path('salir/', views.user_logout, name='salir'),
]
