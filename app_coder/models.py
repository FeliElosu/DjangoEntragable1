from django.db import models

"""
Estudiantes (nombre, apellido, email)
Profesor (nombre, apellido, email, profesion)
Entregable (nombre, fechaDeEntrega, entragado)
curso = (nombre, comision)
"""

class Estudiante(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.EmailField()
    


class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    profesion = models.CharField(max_length=64)
    email = models.EmailField()


class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    comision = models.IntegerField()

class Entregable(models.Model):
    nombre = models.CharField(max_length=128)
    entragado = models.BooleanField()
    fecha_de_entrega = models.DateField()