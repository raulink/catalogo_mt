import sqlite3
import os

# Verificar se o diretório existe ou criá-lo se necessário
db_directory = 'db'
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Conectar ao banco de dados
conn = sqlite3.connect(os.path.join(db_directory, 'dbcat.db'), check_same_thread=False)

def create_table():
    try:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS catalogo 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_almacen TEXT, 
            id_proveedor TEXT, 
            descripcion TEXT, 
            grupo TEXT, 
            subgrupo TEXT, 
            unidad TEXT,
            proveedor TEXT, 
            partida_presupuestaria TEXT, 
            precio_unitario FLOAT, 
            precio_historico FLOAT, 
            precio_usd FLOAT, 
            id_anterior TEXT,
            imagen TEXT, 
            plano TEXT, 
            posicion_plano TEXT, 
            id_plano TEXT, 
            trabajo TEXT, 
            ubicacion TEXT,
            recurrencia TEXT, 
            observaciones TEXT)""")
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error de SQLite durante la creación de la tabla: {e}")

# Chamar a função para criar a tabela
create_table()

# import sqlite3

# conn=sqlite3.connect('db/dbcads.db', check_same_thread=False)

# def create_table():
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS users 
#         (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         name TEXT, 
#         contact TEXT, 
#         age INTEGER, 
#         gender TEXT, 
#         email TEXT, 
#         address TEXT)""")    
#     conn.commit()