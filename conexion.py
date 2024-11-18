import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def __init__(self):
        self.conexion = self.conectar_bd()
    
    def conectar_bd(self):
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='inacap.2024',
                database='crmd'
            )
            if connection.is_connected():
                print("Conexión exitosa a la base de datos")
                self.crear_tablas(connection)
                self.insertar_datos_iniciales(connection)
                return connection
        except Error as e:
            print(f"Error al conectarse a MySQL: {e}")
            return None

    def crear_tablas(self, connection):
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS repartidores (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    precio DECIMAL(10, 2) NOT NULL
                )
            """)
            connection.commit()
            print("Tablas creadas (si no existían)")
        except Error as e:
            print(f"Error al crear tablas: {e}")

    def insertar_datos_iniciales(self, connection):
        try:
            cursor = connection.cursor()
            
            # Comprobar y agregar repartidores si no existen
            repartidores = [
                ('Juan Pérez',),
                ('Ana González',),
                ('Carlos Ramírez',)
            ]
            for repartidor in repartidores:
                cursor.execute("SELECT * FROM repartidores WHERE nombre=%s", (repartidor[0],))
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO repartidores (nombre) VALUES (%s)", repartidor)

            # Comprobar y agregar productos si no existen
            productos = [
                ('Pizza Margarita', 6990),
                ('Hamburguesa Doble', 4990),
                ('Ensalada César', 3990)
            ]
            for producto in productos:
                cursor.execute("SELECT * FROM productos WHERE nombre=%s", (producto[0],))
                if cursor.fetchone() is None:
                    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", producto)

            connection.commit()
            print("Datos iniciales insertados (si no existían)")
        except Error as e:
            print(f"Error al insertar datos iniciales: {e}")

    def cerrar_conexion(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")
