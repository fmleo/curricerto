from django.db import models


class FormacaoNivelChoices(models.TextChoices):
    TECNICO = "TECNICO", "Técnico"
    BACHARELADO = "BACHARELADO", "Bacharelado"
    LICENCIATURA = "LICENCIATURA", "Licenciatura"
    MESTRADO = "MESTRADO", "Mestrado"
    DOUTORADO = "DOUTORADO", "Doutorado"


class NivelChoices(models.TextChoices):
    INICIANTE = "INICIANTE", "Iniciante"
    INTERMEDIARIO = "INTERMEDIARIO", "Intermediário"
    AVANCADO = "AVANCADO", "Avançado"
