from django.db import models

from curriculos.models.choices import NivelChoices
from curriculos.models.user_owned import UserOwned


class Habilidade(UserOwned, models.Model):
    nome = models.CharField("Nome", max_length=100)
    categoria = models.CharField("Categoria", max_length=100)

    nivel = models.CharField("Nível", max_length=20, choices=NivelChoices.choices)

    anos_de_experiencia = models.PositiveIntegerField("Anos de Experiência")

    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"
