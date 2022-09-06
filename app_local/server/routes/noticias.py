from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from server.models.noticias import Noticias, UpdateNoticias


router = APIRouter()


@router.post("/", response_description="Noticia criada no banco")
async def add_noticias(noticia: Noticias) -> dict:
    await noticia.create()
    return {"message": "Noticia criada com sucesso"}


@router.get("/{id}", response_description="Noticia listada")
async def get_noticia_id(id: PydanticObjectId) -> Noticias:
    noticia = await Noticias.get(id)
    return noticia


@router.get("/", response_description="Noticias listadas")
async def get_noticias() -> List[Noticias]:
    noticias = await Noticias.find_all().to_list()
    return noticias


@router.put("/{id}", response_description="Noticia Atualizada")
async def update_noticias_data(id: PydanticObjectId, req: UpdateNoticias) -> Noticias:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    noticia = await Noticias.get(id)
    if not noticia:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma Noticia encontrada!"
    )

    await noticia.update(update_query)
    return noticia


@router.delete("/{id}", response_description="Noticia deletada do Banco de Dados")
async def delete_noticias_data(id: PydanticObjectId) -> dict:
    noticias = await Noticias.get(id)

    if not noticias:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma Noticia encontrada!"
    )

    await noticias.delete()
    return {
        "message": "Noticia Deletada com sucesso"
    }
