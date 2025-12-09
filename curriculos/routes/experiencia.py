from typing import List

from django.http import HttpRequest
from ninja.router import Router

from curriculos.models.experiencia import Experiencia
from curriculos.schemas import ExperienciaSchema, ExperienciaSchemaIn

router = Router(tags=["experiencia"])


@router.get("/", response=List[ExperienciaSchema])
def list(request: HttpRequest):
    """Lista todas as experiências do usuário"""
    return Experiencia.objects.filter(user=request.user)


@router.post("/", response=ExperienciaSchema)
def create(request: HttpRequest, data: ExperienciaSchemaIn):
    """Cria uma nova experiência"""
    experiencia = Experiencia.objects.create(user=request.user, **data.dict())
    return experiencia


@router.put("/{id}")
def update(request: HttpRequest, id: int, data: ExperienciaSchemaIn):
    """Atualiza uma experiência existente"""
    experiencia = Experiencia.objects.get(id=id, user=request.user)
    for key, value in data.dict().items():
        setattr(experiencia, key, value)
    experiencia.save()
    return experiencia


@router.delete("/{id}")
def delete(request: HttpRequest, id: int):
    """Deleta uma experiência existente"""
    experiencia = Experiencia.objects.get(id=id, user=request.user)
    experiencia.delete()
    return {"message": "Experiência deletada com sucesso"}
