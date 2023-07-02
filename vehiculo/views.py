from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout as django_logout


from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    agregar_permiso = request.user.groups.filter(name='grupo1').exists()
    return render(request, 'index.html', {'agregar_permiso': agregar_permiso})

@login_required
def vehiculo_add(request):
    agregar_permiso = request.user.groups.filter(name='grupo1').exists()
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'add.html', {'form': form, 'agregar_permiso': agregar_permiso, 'user': request.user})

@login_required
def vehiculo_list(request):
    agregar_permiso = request.user.groups.filter(name='grupo1').exists()
    vehiculos = Vehiculo.objects.all()
    
    return render(request, 'list.html', {'vehiculos': vehiculos, 'agregar_permiso': agregar_permiso})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar al usuario utilizando las credenciales proporcionadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirigir a la página de "Listar" después del inicio de sesión
    else:
        form = AuthenticationForm(request)
    return render(request, 'custom_login.html', {'form': form})

def custom_logout(request):
    django_logout(request)  # Realizar el logout a través de Django
    return redirect('index')
