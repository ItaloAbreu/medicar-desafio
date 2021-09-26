from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Especialidade(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=240)
    crm = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    telefone = PhoneNumberField(null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade,
                                      on_delete=models.PROTECT,
                                      null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nome} (CRM: {self.crm})'
