from pydantic import BaseModel, EmailStr, validator

# Define el modelo User
class User(BaseModel):
    email: EmailStr  # Valida que el email tenga el formato correcto
    password: str  # Se define como string para la siguiente validacion

    # Valida la contraseña:
    @validator('password')
    def password_validator(cls, value):
        # Valida la longitud
        if len(value) < 6:
            raise ValueError('La contraseña debe tener al menos 6 caracteres')
        # Valida la mayúscula
        if not any(char.isupper() for char in value):
            raise ValueError('La contraseña debe tener al menos una letra mayúscula')
        # Valida el caracter especial
        if not any(char in "!@#$%^&*()" for char in value):
            raise ValueError('La contraseña debe tener al menos un caracter especial')
        return value


# Otro tipo de validacion 
#from pydantic import BaseModel, EmailStr, Field

# Define el modelo User
#class User(BaseModel):
    #email: EmailStr = Field(alias="correo electrónico")  # Valida email y define alias
    #password: str = Field(min_length=6, regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()]).*$")  # Valida contraseña

