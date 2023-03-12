from django.contrib import admin

# Importando tabla productos
from .models import Productos
#Agregando al administrador
admin.site.register(Productos)