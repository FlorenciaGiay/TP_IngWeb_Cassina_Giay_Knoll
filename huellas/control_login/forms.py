from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistro(UserCreationForm):
    nombre_usuario = forms.CharField(max_length=125)
    correo = forms.EmailField(max_length=125)
    clave = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = [
            'nombre_usuario', 
            'correo', 
            'clave',
        ]


class FormInicioSesion(forms.Form):
    correo = forms.EmailField(max_length=125)
    clave = forms.CharField(widget=forms.PasswordInput())


