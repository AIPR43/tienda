from django.db import models

# Create your models here.

class Venta(model.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    Nombre Empleado = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()