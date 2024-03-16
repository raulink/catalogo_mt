from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models import catalogo
from models.catalogo import Catalogo as CatalogoModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.catalogo import CatalogoService
from schemas.catalogo import Catalogo

catalogo_router = APIRouter()
nombre = "catalogo"

#VER CATALOGO
@catalogo_router.get('/catalogo', tags=['catalogo'], response_model=List[Catalogo], status_code=200)# , dependencies=[Depends(JWTBearer())])
def get_catalogo(
    page :int = Query(0,ge=0),
    size :int = Query(10,ge=1,le=100),
    item: str = None
    ): # -> List[Catalogo]:
    db = Session()
    if item is None:
        result = CatalogoService(db).get_catalog(offset=page,limit=size)
    else:
        result = CatalogoService(db).get_catalog_by_item(item)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#BUSCAR ID
@catalogo_router.get('/catalogo/id/{id}', tags=['catalogo'], response_model=List[Catalogo])
def get_catalogo_by_id(id: str = Path(...)):
    db = Session()
    result = CatalogoService(db).get_catalog_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


#BUSCAR CATALOGO
@catalogo_router.get('/catalogo/item/{item}', tags=['catalogo'], response_model=List[Catalogo])
def get_catalogo_by_item(item: str = Path(...)):
    db = Session()
    result = CatalogoService(db).get_catalog_by_item(item)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


#AÑADIR CATALOGO
@catalogo_router.post('/catalogo', tags=['catalogo'], response_model=dict, status_code=201)
def create_catalogo(catalogo: Catalogo):# -> dict:
    db = Session()
    CatalogoService(db).create_catalog(catalogo)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el catalogo"})


#EDITAR CATALOGO
@catalogo_router.put('/catalogo/{id}', tags=['catalogo'], response_model=dict, status_code=200)
def update_catalogo(id: str, catalogo: Catalogo):#-> dict:
    db = Session()
    result = CatalogoService(db).get_catalog(id)
    if not result or result is None:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    CatalogoService(db).update_catalog(id, catalogo)
    return JSONResponse(status_code=200, content={"message": f"Se ha modificado {catalogo.id_almacen}"})


#BORRAR UN CATALOGO
@catalogo_router.delete('/catalogo/{id}', tags=['catalogo'], response_model=dict, status_code=200)
def delete_catalogo(id: str):#-> dict:
    db = Session()
    result: CatalogoModel = db.query(CatalogoModel).filter(CatalogoModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    CatalogoService(db).delete_catalog(id)
    return JSONResponse(status_code=200,  content={"message": f"Se ha eliminado {result.id_almacen}"})