from typing import List

from django.http import HttpRequest
from ninja.router import Router

from curriculos.models.formacao import Formacao
from curriculos.schemas import FormacaoSchema, FormacaoSchemaIn

router = Router(tags=["formacao"])


@router.get("/", response=List[FormacaoSchema])
def list(request: HttpRequest):
    """Lista todas as formações do usuário"""
    return Formacao.objects.filter(user=request.user)


@router.post("/", response=FormacaoSchema)
def create(request: HttpRequest, data: FormacaoSchemaIn):
    """Cria uma nova formação"""
    formacao = Formacao.objects.create(user=request.user, **data.dict())
    return formacao


@router.put("/{id}")
def update(request: HttpRequest, id: int, data: FormacaoSchemaIn):
    """Atualiza uma formação existente"""
    formacao = Formacao.objects.get(id=id, user=request.user)
    for key, value in data.dict().items():
        setattr(formacao, key, value)
    formacao.save()
    return formacao


@router.delete("/{id}")
def delete(request: HttpRequest, id: int):
    """Deleta uma formação existente"""
    formacao = Formacao.objects.get(id=id, user=request.user)
    formacao.delete()
    return {"message": "Formação deletada com sucesso"}
