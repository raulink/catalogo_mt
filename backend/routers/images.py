from fastapi import APIRouter, FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import shutil

import os

app = FastAPI()

images_router = APIRouter()
nombre = "images"

# Ruta para subir imágenes
@images_router.post("/upload/",tags=['images'])
async def upload_image(file: UploadFile = File(...)):
    try:
        # Guardar la imagen en la carpeta 'images'
        with open(f"./assets/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"filename": file.filename}

# Ruta para obtener una lista de imágenes
@images_router.get("/images/",tags=['images'])
async def get_images():
    try:
        # Obtener la lista de archivos en la carpeta 'images'
        files = os.listdir("./assets")
        return {"images": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para obtener una imagen específica por su nombre de archivo
@images_router.get("/images/{image_name}",tags=['images'])
async def get_image(image_name: str):
    try:
        # Verificar si la imagen existe en la carpeta 'images'
        if os.path.exists(f"./assets/{image_name}"):
            return FileResponse(f"./assets/{image_name}")
        else:
            raise HTTPException(status_code=404, detail="Image not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para eliminar una imagen específica por su nombre de archivo
@images_router.delete("/images/{image_name}",tags=['images'])
async def delete_image(image_name: str):
    try:
        # Verificar si la imagen existe en la carpeta 'images'
        if os.path.exists(f"./assets/{image_name}"):
            os.remove(f"./assets/{image_name}")
            return {"message": f"Image {image_name} deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Image not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para actualizar una imagen por su nombre de archivo
@images_router.put("/images/{image_name}",tags=['images'])
async def update_image(image_name: str, file: UploadFile = File(...)):
    try:
        # Verificar si la imagen existe en la carpeta 'images'
        if os.path.exists(f"./assets/{image_name}"):
            # Eliminar la imagen existente
            os.remove(f"./assets/{image_name}")
            # Guardar la nueva imagen
            with open(f"./assets/{file.filename}", "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            return {"message": f"Image {image_name} updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Image not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
