class Repartidor:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()

    def listar(self):
        self.cursor.execute("SELECT * FROM repartidores ORDER BY nombre")
        for repartidor in self.cursor.fetchall():
            print(f"ID: {repartidor[0]}, Nombre: {repartidor[1]}")

    def agregar(self, nombre):
        self.cursor.execute("SELECT * FROM repartidores WHERE nombre=%s", (nombre,))
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO repartidores (nombre) VALUES (%s)", (nombre,))
            self.conexion.commit()
            print(f"Repartidor '{nombre}' agregado exitosamente.")
        else:
            print(f"El repartidor '{nombre}' ya existe.")

    def eliminar(self, id):
        self.cursor.execute("DELETE FROM repartidores WHERE id=%s", (id,))
        self.conexion.commit()
        print(f"Repartidor con ID {id} eliminado exitosamente.")

    def menu(self):
        while True:
            print("\nMenú de Gestión de Repartidores:")
            print("1. Listar repartidores por nombre")
            print("2. Agregar repartidor")
            print("3. Eliminar repartidor")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.listar()
            elif opcion == "2":
                nombre = input("Ingrese el nombre del nuevo repartidor: ")
                self.agregar(nombre)
            elif opcion == "3":
                print("Lista de repartidores disponibles:")
                self.listar()
                id = input("Ingrese el ID del repartidor a eliminar: ")
                self.eliminar(id)
            elif opcion == "4":
                break
            else:
                print("Opción no válida, por favor intenta de nuevo.")
