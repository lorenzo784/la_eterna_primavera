from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import RegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout


class RegisterUser(CreateView):
    model = User
    template_name = 'cuenta/registrar.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('pagina:inicio')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('clinica:formulario')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.name = registerForm.cleaned_data['user_name']
            user.set_password(registerForm.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('clinica:home')
    else:
        registerForm = RegistrationForm()
    return render(request, 'usuario/register.html', {'form': registerForm})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('pagina:inicio')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pagina:inicio')

    else:
        form = UserLoginForm()

    return render(request, 'cuenta/iniciar.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('pagina:inicio')
    