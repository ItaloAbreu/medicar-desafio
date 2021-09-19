import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from especialidades.models import Especialidade
from medicar.utils import SIGLA_ESTADOS


def validar_crm(value: str) -> None:
    """
    CRM é formado somente por números seguido da Sigla do Estado
    Ex: 0000/CE minímo 4 dígitos ou 0000000000/CE máximo 10 dígitos
    """

    regex = r'^[\d].{3,9}\/[a-zA-Z].{1}$'
    if not re.match(regex, value):
        raise ValidationError(
            _("%(value)s não é um CRM válido. Utilize o formato '0000000000/CE'"),
            params={'value': value},
        )
    sigla = value.split('/')[-1]
    if not sigla.upper() in SIGLA_ESTADOS:
        raise ValidationError(
            _(f"{sigla} não corresponde a nenhuma sigla de estado brasileiro."),
            params={'value': value},
        )


class Medico(models.Model):
    nome = models.CharField(max_length=240)
    crm = models.CharField(max_length=13, validators=[validar_crm])
    email = models.EmailField()
    telefone = PhoneNumberField()
    especialidade = models.ForeignKey(Especialidade,
                                      on_delete=models.PROTECT,
                                      null=True, blank=True)
