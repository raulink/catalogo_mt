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