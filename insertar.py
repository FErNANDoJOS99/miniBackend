import os
import django

# Inicializar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from app1.models import Usuario

datos = [
    {"nombre": "Juan", "contraseña": "123"},
    {"nombre": "Maria", "contraseña": "456"},
    {"nombre": "Luis", "contraseña": "789"},
]

for d in datos:
    Usuario.objects.create(**d)

print("Datos insertados correctamente ✅")
