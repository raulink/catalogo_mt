from sqlalchemy import func
from config.database import Session
from models.catalogo import Catalogo  as CatalogoModel
from schemas.catalogo import Catalogo

from sqlalchemy.orm import Session


class CatalogoService():
    
    def __init__(self, db:Session):# -> None: # type: ignore
        self.db:Session = db # type: ignore
        print (type(self.db))

    def get_catalog(self,offset=1,limit=10):
        result = self.db.query(CatalogoModel).offset(offset=offset).limit(limit=limit).all()
        return result

    def get_movie(self, id):
        result = self.db.query(CatalogoModel).filter(CatalogoModel.id == id).first()
        return result

    # Obtener productos por codigo, o descripcion
    def get_catalog_by_item(self, item):
        # Filtrar por categoría utilizando el operador `like`
        # Se busca que la categoría contenga la variable category
        # en cualquier posición, sin importar mayúsculas/minúsculas.
        #result = self.db.query(CatalogoModel).filter(func.lower(CatalogoModel.category).like(f"%{category.lower()}%")).all()
        result = self.db.query(CatalogoModel).filter(
            func.lower(CatalogoModel.descripcion).like(f"%{item.lower()}%") | 
            func.lower(CatalogoModel.id_proveedor).like(f"%{item.lower()}%") | 
            func.lower(CatalogoModel.id_almacen).like(f"%{item.lower()}%")
        ).all()

        #result = self.db.query(CatalogoModel).filter(CatalogoModel.category == category).all()
        return result

    def create_catalog(self, catalogo: Catalogo):
        new_catalog = CatalogoModel(**catalogo.dict())
        self.db.add(new_catalog)
        self.db.commit()
        return
    # Actualizar producto
    def update_catalog(self, id: int, data: Catalogo):
        product = self.db.query(CatalogoModel).filter(CatalogoModel.id == id).first()                
        product.title = data.title
        product.overview = data.overview
        product.year = data.year
        product.rating = data.rating
        product.category = data.category

        self.db.commit()
        return

    def delete_catalog(self, id: int):       
       # self.db.query(CatalogoModel).filter(CatalogoModel.id == id).delete()
       # self.db.commit()
       return