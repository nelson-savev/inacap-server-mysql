from conexion import ConexionBD
from repartidor import Repartidor
from producto import Producto

def main():
    conexion_bd = ConexionBD()
    conexion = conexion_bd.conexion
    
    if conexion:
        gestion_repartidor = Repartidor(conexion)
        gestion_producto = Producto(conexion)

        while True:
            print("\nMenú Principal:")
            print("1. Gestión de Repartidores")
            print("2. Gestión de Productos")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                gestion_repartidor.menu()
            elif opcion == "2":
                gestion_producto.menu()
            elif opcion == "3":
                break
            else:
                print("Opción no válida, por favor intenta de nuevo.")
        
        conexion_bd.cerrar_conexion()

if __name__ == "__main__":
    main()
