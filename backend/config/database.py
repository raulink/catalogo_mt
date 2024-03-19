# Importamos las librerías necesarias

from sqlalchemy import create_engine, MetaData              # Crear la instancia para crear la conexion
from sqlalchemy.ext.declarative import declarative_base     # Crear la instancia para crear declaraciones
from sqlalchemy.orm import sessionmaker

# Replace with your actual connection details
DATABASE_HOST = "zona1.miteleferico.bo"
DATABASE_PORT = 5432
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "postgres"
DATABASE_NAME = "Proy_Catalogo"

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
