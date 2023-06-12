from django.contrib import admin
from .models import Ciudad, Usuario, Playa

# Register your models here.

admin.site.register(Usuario)

admin.site.register(Ciudad)

admin.site.register(Playa)