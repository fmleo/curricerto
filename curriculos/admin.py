# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Certificacao, Experiencia, Formacao, Habilidade, Projeto


@admin.register(Certificacao)
class CertificacaoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "instituicao",
        "data_emissao",
        "data_expiracao",
    )
    list_filter = ("data_emissao", "data_expiracao")


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cargo",
        "empresa",
        "descricao",
        "inicio",
        "fim",
        "em_andamento",
        "localizacao",
        "realizacoes",
    )
    list_filter = ("inicio", "fim", "em_andamento")


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "instituicao",
        "curso",
        "nivel",
        "inicio",
        "fim",
        "em_andamento",
        "descricao",
    )
    list_filter = ("inicio", "fim", "em_andamento")


@admin.register(Habilidade)
class HabilidadeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "categoria",
        "nivel",
        "anos_de_experiencia",
    )


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "descricao",
        "data_inicio",
        "data_fim",
        "link",
    )
    list_filter = ("data_inicio", "data_fim")
    raw_id_fields = ("habilidades",)
