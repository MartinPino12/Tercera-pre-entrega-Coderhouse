from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('usuario', views.usuario, name="Usuario"),
    path('ciudades', views.ciudad, name="Ciudades"),
    path('playas', views.playa, name="Playas"),
    path('newyork', views.newyork, name="New York"),
    path('paris', views.paris, name="Paris"),
    path('sidney', views.sidney, name="Sidney"),
    path('rio', views.rio, name="Rio"),
    path('elcairo', views.elcairo, name="El Cairo"),
    path('bsas', views.bsas, name="Buenos Aires"),
    path('hawai', views.hawai, name="Hawai"),
    path('nazare', views.nazare, name="Nazare"),
    path('miami', views.miami, name="Miami"),
    path('quartapraia', views.quartapraia, name="Quarta Praia"),
    path('playadelcarmen', views.playadelcarmen, name="Playa del Carmen"),
    path('playadepatong', views.playadepatong, name="Playa de Patong"),
    path('ciudadFormulario', views.ciudadFormulario, name="Ciudad Formulario"),
    path('playaFormulario', views.playaFormulario, name="Playa Formulario"),
    path('usuarioFormulario', views.usuarioFormulario, name="Usuario Formulario"),
    path('buscarCiudad', views.buscarCiudad, name="Buscar Ciudad"),
    path('resultadoCiudad', views.resultadoCiudad, name="Resultado Ciudad"),
    path('buscarPlaya', views.buscarPlaya, name="Buscar Playa"),
]