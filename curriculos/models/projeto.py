from django.db import models

from curriculos.models.user_owned import UserOwned


class Projeto(UserOwned, models.Model):
    nome = models.CharField("Nome", max_length=100)
    descricao = models.TextField("Descrição")
    data_inicio = models.DateField("Data de Início")
    data_fim = models.DateField("Data de Fim")
    habilidades = models.ManyToManyField("Habilidade", verbose_name="Habilidades")
    link = models.URLField("Link")

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
