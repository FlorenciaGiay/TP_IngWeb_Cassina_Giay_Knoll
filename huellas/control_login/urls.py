from django.urls import path
from .views import inicio, inicio_sesion, registro
from django.conf import settings

urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio/', inicio, name="inicio"),
    path('inicio_sesion/', inicio_sesion, name="inicio_sesion"),
    path('registro/', registro, name="registro"),
]