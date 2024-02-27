import os

class Producto:
    def __init__(self, codigoProducto, nombreProducto, descripcionProducto, precioProducto ) -> None:
        self.codigoProducto = codigoProducto
        self.nombreProducto = nombreProducto
        self.descripcionProducto = descripcionProducto
        self.precioProducto = precioProducto

lista_Producto = []
def main():
    print("================================")
    print("       Bienvenido al menú       ")
    print("================================")
    print("1. Registrar Producto           ")
    print("2. Registrar Cliente            ")
    print("3. Realizar Compra              ")
    print("4. Reporte de Compra            ")
    print("5. Datos del Estudiante         ")
    print("6. Salir")
    print("================================")
    opcion = input("Seleccione una opción a realizar")

    if opcion == "1":
        RegistrarProducto()
    elif opcion == "2":
        RegistrarProducto()
    else:
        print("opcion invalida")
        main()
        


def RegistrarProducto():
    codigoProducto = input("Ingrese Producto")
    
