from django.urls import path
from .views import perdidos, publicar_perdidos
from django.conf import settings

urlpatterns = [
    path('', perdidos, name="perdidos"),
    path('perdidos/', perdidos, name="perdidos"),
    path('publicar_perdidos/', publicar_perdidos, name="publicar_perdidos"),
]