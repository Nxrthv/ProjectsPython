import sqlite3

class Conexion():
    def __init__(self):
        self.base_datos = 'Database/Inventario.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def Cerrar(self):
        self.conexion.commit()
        self.conexion.close()