from typing import List

from django.http import HttpRequest
from ninja.router import Router

from curriculos.models.certificacao import Certificacao
from curriculos.schemas import ExperienciaSchema, ExperienciaSchemaIn

router = Router(tags=["certificacao"])


@router.get("/", response=List[ExperienciaSchema])
def list(request: HttpRequest):
    """Lista todas as certificações do usuário"""
    return Certificacao.objects.filter(user=request.user)


@router.post("/", response=ExperienciaSchema)
def create(request: HttpRequest, data: ExperienciaSchemaIn):
    """Cria uma nova certificação"""
    certificacao = Certificacao.objects.create(user=request.user, **data.dict())
    return certificacao


@router.put("/{id}")
def update(request: HttpRequest, id: int, data: ExperienciaSchemaIn):
    """Atualiza uma certificação existente"""
    certificacao = Certificacao.objects.get(id=id, user=request.user)
    for key, value in data.dict().items():
        setattr(certificacao, key, value)
    certificacao.save()
    return certificacao


@router.delete("/{id}")
def delete(request: HttpRequest, id: int):
    """Deleta uma certificação existente"""
    certificacao = Certificacao.objects.get(id=id, user=request.user)
    certificacao.delete()
    return {"message": "Certificação deletada com sucesso"}
