from ninja import ModelSchema

from curriculos.models.certificacao import Certificacao
from curriculos.models.experiencia import Experiencia
from curriculos.models.formacao import Formacao
from curriculos.models.habilidade import Habilidade
from curriculos.models.projeto import Projeto


class CertificacaoSchema(ModelSchema):
    class Meta:
        model = Certificacao
        exclude = ["user"]


class CertificacaoSchemaIn(ModelSchema):
    class Meta:
        model = Certificacao
        exclude = ["user", "id"]


class ExperienciaSchema(ModelSchema):
    class Meta:
        model = Experiencia
        exclude = ["user"]


class ExperienciaSchemaIn(ModelSchema):
    class Meta:
        model = Experiencia
        exclude = ["user", "id"]


class FormacaoSchema(ModelSchema):
    class Meta:
        model = Formacao
        exclude = ["user"]


class FormacaoSchemaIn(ModelSchema):
    class Meta:
        model = Formacao
        exclude = ["user", "id"]


class HabilidadeSchema(ModelSchema):
    class Meta:
        model = Habilidade
        exclude = ["user"]


class HabilidadeSchemaIn(ModelSchema):
    class Meta:
        model = Habilidade
        exclude = ["user", "id"]


class ProjetoSchema(ModelSchema):
    class Meta:
        model = Projeto
        exclude = ["user"]


class ProjetoSchemaIn(ModelSchema):
    class Meta:
        model = Projeto
        exclude = ["user", "id"]
