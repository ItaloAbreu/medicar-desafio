from django.db import models
from django.contrib.postgres.fields import ArrayField
from medicos.models import Medico


class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField()
    horarios = ArrayField(models.TimeField())
