from django import forms


class CiudadFormulario(forms.Form):
    nombre = forms.CharField()
    pais = forms.CharField()

class PlayaFormulario(forms.Form):
    nombre = forms.CharField()
    pais = forms.CharField()

class UsuarioFormulario(forms.Form):
    usuario = forms.CharField()
    email = forms.CharField()