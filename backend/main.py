# Importamos las librerías necesarias
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Importamos la configuración y los middlewares
from config.database import engine, Base  # Importamos la configuración de la base de datos

from middlewares.error_handler import ErrorHandler  # Importamos el middleware de gestión de errores

# Importamos los routers para diferentes funcionalidades
from routers.movie import movie_router
from routers.user import user_router
from routers.catalogo import catalogo_router
from routers.images import images_router

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
app.include_router(catalogo_router)  # Incluimos el router de películas
app.include_router(images_router)  # Incluimos el router de imagenes

# Creamos todas las tablas en la base de datos a partir de los modelos definidos en otro lugar
#Base.metadata.create_all(bind=engine)  # Creamos las tablas de la base de datos a partir de los modelos

# Definimos un endpoint raíz para la aplicación
@app.get('/', tags=['home'])
def message():
    """
    Este endpoint devuelve un mensaje simple como respuesta.
    Sirve como un endpoint de verificación básica del estado de la aplicación.
    """
    return HTMLResponse('<h1>Hola mundo</h1>')

