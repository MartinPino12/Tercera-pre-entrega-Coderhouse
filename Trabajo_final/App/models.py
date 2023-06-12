from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=20)

class Playa(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=20)
