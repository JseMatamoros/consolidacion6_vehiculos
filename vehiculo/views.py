from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout as django_logout
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def vehiculo_add(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_list')
    else:
        form = VehiculoForm()
    return render(request, 'add.html', {'form': form, 'user': request.user})

@login_required
def vehiculo_list(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'list.html', {'vehiculos': vehiculos})

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
                return redirect('index')  # Redirigir a la página de inicio después del inicio de sesión
    else:
        form = AuthenticationForm(request)
    return render(request, 'custom_login.html', {'form': form})

def custom_logout(request):
    django_logout(request)  # Realizar el logout a través de Django
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página principal después del registro
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
