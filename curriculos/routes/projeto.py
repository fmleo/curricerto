from typing import List

from django.http import HttpRequest
from ninja.router import Router

from curriculos.models.projeto import Projeto
from curriculos.schemas import ProjetoSchema, ProjetoSchemaIn

router = Router(tags=["projeto"])


@router.get("/", response=List[ProjetoSchema])
def list(request: HttpRequest):
    """Lista todos os projetos do usuário"""
    return Projeto.objects.filter(user=request.user)


@router.post("/", response=ProjetoSchema)
def create(request: HttpRequest, data: ProjetoSchemaIn):
    """Cria um novo projeto"""
    projeto = Projeto.objects.create(user=request.user, **data.dict())
    return projeto


@router.put("/{id}")
def update(request: HttpRequest, id: int, data: ProjetoSchemaIn):
    """Atualiza um projeto existente"""
    projeto = Projeto.objects.get(id=id, user=request.user)
    for key, value in data.dict().items():
        setattr(projeto, key, value)
    projeto.save()
    return projeto


@router.delete("/{id}")
def delete(request: HttpRequest, id: int):
    """Deleta um projeto existente"""
    projeto = Projeto.objects.get(id=id, user=request.user)
    projeto.delete()
    return {"message": "Projeto deletado com sucesso"}
