from typing import List

from django.http import HttpRequest
from ninja.router import Router

from curriculos.models.habilidade import Habilidade
from curriculos.schemas import HabilidadeSchema, HabilidadeSchemaIn

router = Router(tags=["habilidade"])


@router.get("/", response=List[HabilidadeSchema])
def list(request: HttpRequest):
    """Lista todas as habilidades do usuário"""
    return Habilidade.objects.filter(user=request.user)


@router.post("/", response=HabilidadeSchema)
def create(request: HttpRequest, data: HabilidadeSchemaIn):
    """Cria uma nova habilidade"""
    habilidade = Habilidade.objects.create(user=request.user, **data.dict())
    return habilidade


@router.put("/{id}")
def update(request: HttpRequest, id: int, data: HabilidadeSchemaIn):
    """Atualiza uma habilidade existente"""
    habilidade = Habilidade.objects.get(id=id, user=request.user)
    for key, value in data.dict().items():
        setattr(habilidade, key, value)
    habilidade.save()
    return habilidade


@router.delete("/{id}")
def delete(request: HttpRequest, id: int):
    """Deleta uma habilidade existente"""
    habilidade = Habilidade.objects.get(id=id, user=request.user)
    habilidade.delete()
    return {"message": "Habilidade deletada com sucesso"}
