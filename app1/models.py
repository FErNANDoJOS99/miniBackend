from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=128)  # se recomienda encriptarla

    def __str__(self):
        return self.nombre


class Cancion(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,  # Si se borra el usuario, se borran sus canciones
        related_name="canciones"   # permite acceder con usuario.canciones.all()
    )

    def __str__(self):
        return self.nombre
