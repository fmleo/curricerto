from django.db import models

from curriculos.models.choices import FormacaoNivelChoices
from curriculos.models.user_owned import UserOwned


class Formacao(UserOwned, models.Model):
    instituicao = models.CharField("Instituição", max_length=100)
    curso = models.CharField("Curso", max_length=100)

    nivel = models.CharField(
        "Nível", max_length=20, choices=FormacaoNivelChoices.choices
    )

    inicio = models.DateField("Início")
    fim = models.DateField("Fim")

    em_andamento = models.BooleanField("Em Andamento", default=False)

    descricao = models.TextField("Descrição")

    class Meta:
        verbose_name = "Formação"
        verbose_name_plural = "Formações"
