from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Catalogo(Base):
    __tablename__ = "catalogo"  # Define el nombre de la tabla

    id = Column(Integer, primary_key=True, index=True)  # Clave primaria y con índice
    descripcion = Column(String(255))
    id_proveedor = Column(String(255))
    id_almacen = Column(String(255))
    precio_unitario = Column(Float)
    precio_unitario_historico = Column(Float)
    precio_unitario_usd = Column(Float)
    id_anterior = Column(String(255))
    unidad = Column(String(255))
    grupo = Column(String(255))
    sub_grupo = Column(String(255))
    partida_presupuestaria = Column(String(255))
    proveedor = Column(String(255))
    imagen = Column(String(255))
    plano = Column(String(255))
    posicion_plano = Column(String(255))
    id_plano = Column(String(255))
    ubicacion = Column(String(255))
    trabajo = Column(String(255))
    recurrencia = Column(String(255))
    observaciones = Column(String(255))

    def __repr__(self):
        return f"Catalogo(id={self.id}, descripcion='{self.descripcion}')"
