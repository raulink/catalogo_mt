# FastAPI - Flet

Crear una nueva entidad en la base de datos

# Programa principal

```python
# Importamos las librerías necesarias
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Importamos la configuración y los middlewares
from config.database import engine, Base  # Importamos la configuración de la base de datos

from middlewares.error_handler import ErrorHandler  # Importamos el middleware de gestión de errores

# Importamos los routers para diferentes funcionalidades
from routers.movie import movie_router
from routers.user import user_router

# Creamos la instancia de la aplicación FastAPI
app = FastAPI()

# Configuramos la información de la aplicación
app.title = "Aplicación de catálogo de Items"  # Establecemos el título de la aplicación
app.version = "0.0.2"  # Establecemos la versión de la aplicación

# Añadimos el middleware para la gestión de errores
app.add_middleware(ErrorHandler)  # Añadimos el middleware de gestión de errores

# Incluimos los routers para diferentes funcionalidades
app.include_router(movie_router)  # Incluimos el router de películas
app.include_router(user_router)   # Incluimos el router de usuarios

# Creamos todas las tablas en la base de datos a partir de los modelos definidos en otro lugar
Base.metadata.create_all(bind=engine)  # Creamos las tablas de la base de datos a partir de los modelos

# Definimos un endpoint raíz para la aplicación
@app.get('/', tags=['home'])
def message():
    """
    Este endpoint devuelve un mensaje simple como respuesta.
    Sirve como un endpoint de verificación básica del estado de la aplicación.
    """
    return HTMLResponse('<h1>Hola mundo</h1>')
```

## Estructura de las carpetas

El programa tiene la siguiente estructura:

```
│   main.py  (Programa principal)
│   requiremets.txt  (requerimientos del sistema)
├───config            (configuracion de la base de datos)
│   │   database.py
├───middlewares 
│   │   error_handler.py
│   │   jwt_bearer.py
├───models (Modelos en la base de datos)
│   │   movie.py
│   │   user.py
├───routers (Rutas)
│   │   movie.py
│   │   user.py
├───schemas (Esquemas y validaciones)
│   │   movie.py
│   │   user.py
├───services (servicios)
│   │   movie.py
│   │   users.py
├───utils    (Otras utilidades)
│   │   jwt_manager.py
```

# Conexión a la base de datos

- Conexión con una base de datos SQLite
    
    ```python
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    
    sqlite_file_name = "../database.sqlite"
    base_dir = os.path.dirname(os.path.realpath(__file__))
    
    database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
    
    engine = create_engine(database_url, echo=True)
    
    Session = sessionmaker(bind=engine)
    
    Base = declarative_base()
    ```
    
- Conexión con una base de datos PostgreSQL
    
    ```python
    # Importamos las librerías necesarias
    
    from sqlalchemy import create_engine, MetaData              # Crear la instancia para crear la conexion
    from sqlalchemy.ext.declarative import declarative_base     # Crear la instancia para crear declaraciones
    from sqlalchemy.orm import sessionmaker
    
    # Replace with your actual connection details
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 5434
    DATABASE_USER = "openpg"
    DATABASE_PASSWORD = "openpgpwd"
    DATABASE_NAME = "peliculas"
    
    # Build the connection string
    DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    
    # Create the engine
    engine = create_engine(DATABASE_URL, echo=True)
    
    # Create the metadata object (optional)
    metadata = MetaData()
    
    # Create the session class
    Session = sessionmaker(bind=engine)
    
    # Create the declarative base class
    Base = declarative_base()
    Base.metadata = metadata
    ```
    
- Base de datos MySQL
    
    ```python
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    
    # Configuración de la conexión a la base de datos MySQL
    user = 'tu_usuario_mysql'
    password = 'tu_contraseña_mysql'
    host = 'localhost'
    database_name = 'nombre_de_tu_base_de_datos_mysql'
    
    # Cadena de conexión MySQL
    database_url = f"mysql+pymysql://{user}:{password}@{host}/{database_name}"
    
    # Crea el motor de la base de datos
    engine = create_engine(database_url, echo=True)
    
    # Crea una sesión
    Session = sessionmaker(bind=engine)
    
    # Crea una clase base declarativa para definir las clases de modelos
    Base = declarative_base()
    ```
    

# 1. Modelo

Modelo usuarios:

```python
from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)        
```

# 2. Esquema

Los esquemas definen la estructura de los datos que se manejan de la entidad, permiten validaciones, y definiciones de si son campos obligatorios u opcionales, además de valores por defecto. 

**Por ejemplo:** Realiza la validacion del siguiente esquema, el email validar que tenga el formato email con @ y el password que tenga 1 caracter mayuscula 1 caracter especial y una longitud de 6 minimo:

```python
from pydantic import BaseModel, EmailStr, Field

# Define el modelo User
class User(BaseModel):
    email: EmailStr = Field(alias="correo electrónico")  # Valida email y define alias
    password: str = Field(min_length=6, regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()]).*$")  # Valida contraseña
```

# 3. Servicio

```python
from models.user import User as UserModel   # Importar el modelo y la base de datos
from schemas.user import User   # Importar el esquema

class UserService():
    
    def __init__(self, db): # -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all() # Obtener todos los usuarios
        return result

    def get_user(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result

    def create_user(self, user: User):
        new_user = UserModel(**user.dict()) # Descompone el usuario en un diccionario con **user.dict()
        self.db.add(new_user)   # Añadir nuevo usuario 
        self.db.commit()        # Añadir los cambiso en la base de datos
        return

    def update_user(self, id: int, data: User):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()  # Buscar el usuario que coincide con el id
        user.email = data.email         # Obtener el email de los datos enviados
        user.password = data.password   # Obtener el password de los datos enviados
        self.db.commit()                # Almacenar los datos en la base de datos
        return

    def delete_user(self, id: int):
       self.db.query(UserModel).filter(UserModel.id == id).delete() # Eliminar usuario
       self.db.commit()     # Guardar los datos en la base de datos
       return
```

# 4. Rutas

```python
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

```
