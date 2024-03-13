from pydantic import BaseModel, EmailStr, Field

class Catalogo(BaseModel):
    id: int  # Clave primaria
    id_almacen: str  # Identificador del almacén
    id_proveedor: str  # Identificador del proveedor
    descripcion: str  # Descripción del producto
    grupo: str  # Grupo al que pertenece el producto
    subgrupo: str  # Subgrupo al que pertenece el producto
    unidad: str  # Unidad de medida del producto
    proveedor: str  # Nombre del proveedor
    partida_presupuestaria: str  # Partida presupuestaria asociada al producto
    precio_unitario: float  # Precio unitario del producto
    precio_historico: float  # Precio unitario histórico del producto
    precio_usd: float  # Precio unitario en USD
    id_anterior: str  # Identificador anterior del producto
    imagen: str  # Ruta de la imagen del producto
    plano: str  # Plano donde se encuentra el producto
    posicion_plano: str  # Posición del producto en el plano
    id_plano: str  # Identificador del plano
    trabajo: str  # Trabajo asociado al producto
    ubicacion: str  # Ubicación física del producto
    recurrencia: str  # Recurrencia del producto
    observaciones: str  # Observaciones adicionales del producto

    class Config:
        orm_mode = True  # Indica que este modelo se usará con SQLAlchemy