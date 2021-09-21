from django.db import models
from django.contrib.postgres.fields import ArrayField
from medicos.models import Medico


class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{dia} {horario} com {medico}'.format(
            dia=self.dia,
            horario=self.horario,
            medico=self.medico,
        )


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField()
    horarios = ArrayField(models.TimeField())

    def __str__(self) -> str:
        return  '{dia} com {medico}'.format(
            dia=self.dia,
            medico=self.medico,
        )
