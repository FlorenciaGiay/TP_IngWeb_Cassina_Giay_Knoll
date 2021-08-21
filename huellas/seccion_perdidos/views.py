from django.shortcuts import render

def perdidos(request):
    return render(request, 'perdidos.html', {})

def publicar_perdidos(request):
    return render(request, 'publicar_perdidos.html', {})
