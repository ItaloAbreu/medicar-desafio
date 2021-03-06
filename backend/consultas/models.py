from datetime import date
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
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

    def horarios_disponiveis(self):
        now = timezone.localtime()
        return self.horarioagenda_set.filter(agenda=self, disponivel=True).exclude(
            agenda__dia=now,
            horario__hour__lte=now.hour,
            horario__minute__lte=now.minute
        )


class HorarioAgenda(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    horario = models.TimeField()
    disponivel = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        unique_together = ('horario', 'agenda')

    def __str__(self) -> str:
        return f'{self.horario}'


class Consulta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    horario = models.TimeField()
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(
        auto_created=True, auto_now_add=True, editable=False)

    def rn_dia_passado(self):
        today = date.today()
        if self.agenda.dia < today:
            return False
        return True

    def rn_horario_passado(self):
        today = date.today()
        now = timezone.localtime()
        if self.agenda.dia == today and (self.horario.hour < now.hour
                                         or (self.horario.hour == now.hour
                                             and self.horario.minute <= now.minute)):
            return False
        return True

    def rn_usuario_agendado_em_dia_hora(self):
        consulta = Consulta.objects.filter(
            usuario=self.usuario, horario=self.horario, agenda__dia=self.agenda.dia)
        return not consulta.exists()

    def rn_dia_horario_disponveis(self):
        horarioagenda = HorarioAgenda.objects.filter(
            horario=self.horario, agenda=self.agenda, disponivel=True)
        return horarioagenda.exists()

    def clean(self):
        if not self.rn_dia_passado():
            raise ValidationError(
                "Não é possível agendar uma consulta em um dia passado.")
        if not self.rn_horario_passado():
            raise ValidationError(
                "Não é possível agendar uma consulta em um horário passado.")
        if not self.rn_usuario_agendado_em_dia_hora():
            raise ValidationError(
                "Usuário já está agendado para esse dia e horário.")
        if not self.rn_dia_horario_disponveis():
            raise ValidationError(
                "Horário da agenda não está disponível.")

    def __str__(self) -> str:
        return '{dia} {horario} com {medico}'.format(
            dia=self.agenda.dia,
            horario=self.horario,
            medico=self.agenda.medico,
        )


def alterar_disponibilidade_horarioagenda(consulta, disponibilidade):
    horarioagenda = HorarioAgenda.objects.filter(
        agenda=consulta.agenda, horario=consulta.horario).first()
    if not horarioagenda:
        return
    horarioagenda.disponivel = disponibilidade
    horarioagenda.save()


@receiver(post_save, sender=Consulta)
def indisponibilizar_horarioagenda(instance, created, *args, **kwargs):
    if not created:
        return
    alterar_disponibilidade_horarioagenda(instance, False)


@receiver(post_delete, sender=Consulta)
def disponibilizar_horarioagenda(instance, *args, **kwargs):
    alterar_disponibilidade_horarioagenda(instance, True)
