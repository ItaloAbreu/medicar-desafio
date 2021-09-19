from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(max_length=120)
