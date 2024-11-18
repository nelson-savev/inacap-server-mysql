class Producto:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = conexion.cursor()

    def listar(self):
        self.cursor.execute("SELECT * FROM productos ORDER BY nombre")
        for producto in self.cursor.fetchall():
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]} CLP")

    def agregar(self, nombre, precio):
        self.cursor.execute("SELECT * FROM productos WHERE nombre=%s", (nombre,))
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", (nombre, precio))
            self.conexion.commit()
            print(f"Producto '{nombre}' con precio {precio} CLP agregado exitosamente.")
        else:
            print(f"El producto '{nombre}' ya existe.")

    def eliminar(self, id):
        self.cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
        self.conexion.commit()
        print(f"Producto con ID {id} eliminado exitosamente.")

    def menu(self):
        while True:
            print("\nMenú de Gestión de Productos:")
            print("1. Listar productos por nombre")
            print("2. Agregar producto")
            print("3. Eliminar producto")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.listar()
            elif opcion == "2":
                nombre = input("Ingrese el nombre del nuevo producto: ")
                precio = input("Ingrese el precio del nuevo producto: ")
                try:
                    precio = float(precio)
                    self.agregar(nombre, precio)
                except ValueError:
                    print("Precio no válido. Por favor, ingresa un número.")
            elif opcion == "3":
                print("Lista de productos disponibles:")
                self.listar()
                id = input("Ingrese el ID del producto a eliminar: ")
                self.eliminar(id)
            elif opcion == "4":
                break
            else:
                print("Opción no válida, por favor intenta de nuevo.")
