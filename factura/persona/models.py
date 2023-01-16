from django.db import models
class Persona(models.Model):
    nombre = models.CharField(max_length=80)
    cedula = models.IntegerField()
    fecha_nacimiento = models.DateField(auto_now=False,auto_now_add=False)