from django.db import models

from curriculos.models.user_owned import UserOwned


class Certificacao(UserOwned, models.Model):
    nome = models.CharField("Nome", max_length=100)
    instituicao = models.CharField("Instituição", max_length=100)
    data_emissao = models.DateField("Data de Emissão")
    data_expiracao = models.DateField("Data de Expiração")

    class Meta:
        verbose_name = "Certificação"
        verbose_name_plural = "Certificações"
