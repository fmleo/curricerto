from django.db import models

from curriculos.models.user_owned import UserOwned


class Experiencia(UserOwned, models.Model):
    cargo = models.CharField("Cargo", max_length=100)
    empresa = models.CharField("Empresa", max_length=100)
    descricao = models.TextField("Descrição")
    inicio = models.DateField("Início")
    fim = models.DateField("Fim")
    em_andamento = models.BooleanField("Em Andamento", default=False)
    localizacao = models.CharField("Localização", max_length=100)
    realizacoes = models.JSONField("Realizações", default=list)

    class Meta:
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"
