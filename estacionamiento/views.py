
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.context_processors import request
from django.urls import reverse
from django.utils import timezone



def login_view(request):
   
    if request.method == 'POST':
        username = request.POST['txtuser'].lower()
        password = request.POST['txtpass']
        user = authenticate(request,username = username, password=password)
        if user:
            login(request,user) 
            return HttpResponseRedirect(reverse('mapa'))
        else:
            
            return render(request, 'carts/login.html',context)
    else:
        
        return render(request,'carts/login.html',context) 
@login_required(login_url='login')
def logout_view(request):
  
    if request.method == 'POST':
        logout(request)
    return redirect('login')
def mapa(request):
    return render(request,'estacionamiento/mapa.html')

def registro_normal(request):
    user = User()
    if request.method == 'POST':
        pass
    return render(request,'estacionamiento/registro_normal.html')
