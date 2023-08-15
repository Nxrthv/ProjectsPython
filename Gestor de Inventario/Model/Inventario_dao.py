from .Conexion import Conexion

def Crear_Tabla():
    conexion = Conexion()

    sql = '''
    CREATE TABLE Inventario(
        ID INTEGER,
        Nombre VARCHAR(100),
        Precio VARCHAR(10),
        Disponible VARCHAR(25),
        PRIMARY KEY(ID AUTOINCREMENT)
    )'''

    conexion.cursor.execute(sql)
    conexion.Cerrar()

def Borrar_Tabla():
    conexion = Conexion()

    sql = 'DROP TABLE Inventario'

    conexion.cursor.execute(sql)
    conexion.Cerrar()
