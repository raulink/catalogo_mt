from fastapi import APIRouter               # Para permitir colocara rutas en otros archivos
from fastapi import Depends, Path, Query    # Para utilizar depends y proteger las rutas
from fastapi.encoders import jsonable_encoder   # Codificador Json

from middlewares.jwt_bearer import JWTBearer
from utils.jwt_manager import create_token  
from fastapi.responses import JSONResponse

from typing import Optional, List
from config.database import Session # Sesion de la base de datos


from models.user import User as UserModel
from schemas.user import User
from services.users import UserService



user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    


@user_router.get('/users', tags=['users'], response_model=List[User], status_code=200, dependencies=[Depends(JWTBearer())])
def get_users(): # -> List[User]:
    db = Session()    
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.get('/users/{id}', tags=['users'], response_model=User)
def get_user(id: int = Path(ge=1, le=2000)): # -> Movie:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.post('/users', tags=['users'], response_model=dict, status_code=201)
def create_user(user: User):# -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el usuario"})

@user_router.put('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def update_user(id: int, user: User):#-> dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})    
    UserService(db).update_user(id, user)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el usuario"})


@user_router.delete('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def delete_movie(id: int):#-> dict:
    db = Session()
    result: UserService = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    UserService(db).delete_user(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado El usuario"})
