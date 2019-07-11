
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import request
from django.urls import reverse
from django.utils import timezone
from .models import Perfil


def login_view(request):
   
    if request.method == 'POST':
        username = request.POST['txtuser'].lower()
        password = request.POST['txtpass']
        user = authenticate(request,username = username, password=password)
        if user:
            login(request,user) 
            return HttpResponseRedirect(reverse('mapa'))
        else:
            
            return render(request, 'estacionamiento/login.html')
    else:
        
        return render(request,'estacionamiento/login.html') 
@login_required(login_url='login')
def logout_view(request):
  
    if request.method == 'POST':
        logout(request)
    return redirect('login')
def mapa(request):
    return render(request,'estacionamiento/mapa.html')

def registro_normal(request):
    user = User()

    alert = 'verde'
    if request.method == 'POST':
        try:
            user = User.objects.create_user(username=request.POST.get('txtemail'),password=request.POST.get('txtpass'))
            mensaje = 'Registrado como arrendatario'
        except:
            messages.success(request,'Usuario ya registrado')
            alert = 'roja'          
            variables = {'alert':alert} 
            return render(request,'estacionamiento/registro_normal.html',variables)
        user.email = request.POST.get('txtemail')
        user.first_name = request.POST.get('txtnombre')
        user.last_name = request.POST.get('txtapellido')
        user.perfil.fecha_nacimiento = requets.POST.get('txtfecha')
        user.perfil.telefono  = request.POST.get('txttelefono')
        user.perfil.direccion = request.POST.get('txtdireccion')
        user.perfil.tipo = 'Normal'
        messages.error(request,mensaje)
        user.save()
        # AQUI QUEDEE
    return render(request,'estacionamiento/registro_normal.html')
