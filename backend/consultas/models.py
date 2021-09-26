from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from medicos.models import Medico


def date_in_the_past(value) -> None:
    now = date.today()
    if value < now:
        raise ValidationError(
            _("Não é possível criar uma agenda em um dia passado."),
            params={'value': value},
        )


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(validators=[date_in_the_past])

    class Meta:
        unique_together = ('medico', 'dia')

    def __str__(self) -> str:
        return '{medico} em {dia}'.format(
            medico=self.medico,
            dia=self.dia,
        )


class HorarioAgenda(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    horario = models.TimeField()

    class Meta:
        unique_together = ('horario', 'agenda')

    def __str__(self) -> str:
        return f'{self.horario}'


class Consulta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(
        auto_created=True, auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return '{dia} {horario} com {medico}'.format(
            dia=self.agenda.dia,
            horario=self.horario,
            medico=self.agenda.medico,
        )
