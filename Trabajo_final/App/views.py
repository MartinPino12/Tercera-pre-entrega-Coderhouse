from django.shortcuts import render, HttpResponse
from App.forms import CiudadFormulario, PlayaFormulario, UsuarioFormulario
from .models import Ciudad, Playa, Usuario
# Create your views here.

def inicio(request):
    return render(request, "App/index.html")

def usuario(request):
    return render(request, "App/usuario.html")

def ciudad(request):
    return render(request, "App/ciudad.html")

def playa(request):
    return render(request, "App/playa.html")

def newyork(request):
    return render(request, "App/newyork.html")

def paris(request):
    return render(request, "App/paris.html")

def sidney(request):
    return render(request, "App/sidney.html")

def rio(request):
    return render(request, "App/rio.html")

def elcairo(request):
    return render(request, "App/elcairo.html")

def bsas(request):
    return render(request, "App/bsas.html")

def hawai(request):
    return render(request, "App/hawai.html")

def nazare(request):
    return render(request, "App/nazare.html")

def miami(request):
    return render(request, "App/miami.html")

def quartapraia(request):
    return render(request, "App/quartapraia.html")

def playadelcarmen(request):
    return render(request, "App/playadelcarmen.html")

def playadepatong(request):
    return render(request, "App/playadepatong.html")

def ciudadFormulario(request):
    
    if request.method == "POST":
        miFormulario = CiudadFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            ciudad = Ciudad(nombre=informacion["nombre"], pais=informacion["pais"])
            ciudad.save()
            return render(request, "App/ciudad.html")
    else:
        miFormulario = CiudadFormulario()

    return render(request, "App/ciudadFormulario.html", {"miFormulario": miFormulario})

def playaFormulario(request):
    
    if request.method == "POST":
        miFormulario = PlayaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            playa = Playa(nombre=informacion["nombre"], pais=informacion["pais"])
            playa.save()
            return render(request, "App/playa.html")
    else:
        miFormulario = PlayaFormulario()

    return render(request, "App/playaFormulario.html", {"miFormulario": miFormulario})

def usuarioFormulario(request):
    
    if request.method == "POST":
        miFormulario = UsuarioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario = Usuario(nombre=informacion["usuario"], email=informacion["email"])
            usuario.save()
            return render(request, "App/usuario.html")
    else:
        miFormulario = UsuarioFormulario()

    return render(request, "App/usuarioFormulario.html", {"miFormulario": miFormulario})

def buscarCiudad(request):
    nombre = request.GET.get("nombre", "")
    
    if nombre:
        ciudades = Ciudad.objects.filter(nombre__icontains=nombre)
        return render(request, "App/resultadoCiudad.html", {"ciudades": ciudades, "nombre": nombre})
    
    return render(request, "App/buscarCiudad.html")

def resultadoCiudad(request):
    return render(request, "App/resultadoCiudad.html")

def buscarPlaya(request):
    nombre = request.GET.get("nombre", "")
    
    if nombre:
        playas = Playa.objects.filter(nombre__icontains=nombre)
        return render(request, "App/resultadoPlaya.html", {"playas": playas, "nombre": nombre})
    
    return render(request, "App/buscarPlaya.html")