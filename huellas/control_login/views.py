from django.shortcuts import render, redirect
from control_login.forms import FormInicioSesion, FormRegistro

def inicio(request):
    return render(request, 'inicio.html', {})

def inicio_sesion(request):
    if request.method=="POST":
        form = FormInicioSesion(request.POST)
    else:
        form = FormInicioSesion()
    return render(request, 'inicio_sesion.html', {'form':form})

def registro(request):
    if request.method=="POST":
        form = FormRegistro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = FormRegistro()  
    return render(request,'registro.html', {'form': form})