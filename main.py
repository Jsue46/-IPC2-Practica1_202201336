import os

class Producto:
    def __init__(self, codigoProducto, nombreProducto, descripcionProducto, precioProducto ) -> None:
        self.codigoProducto = codigoProducto
        self.nombreProducto = nombreProducto
        self.descripcionProducto = descripcionProducto
        self.precioProducto = precioProducto
lista_Producto = []

class Cliente:
    def __init__(self, nombreCliente, correoCliente, nitCliente) -> None:
        self.nombreCliente = nombreCliente
        self.correoCliente = correoCliente
        self.nitCliente = nitCliente
lista_Cliente = []

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
    opcion = input("Seleccione una opción a realizar  ")

    if opcion == "1":
        RegistrarProducto()
    elif opcion == "2":
        RegistrarCliente()
    elif opcion == "5":
        print("==============================")
        print("    Datos del estdiante       ")
        print(" Estuardo Josué Vaquiax Reyes ")
        print("          202201336           ")
        print("==============================")
        main()
    elif opcion == "6":
        #os.system('clear')
        print("Gracias por usar el sistema")
    else:
        print("opcion invalida")
        main()
        
def RegistrarProducto():
    print("================================")
    print("       Registrar Producto       ")
    print("================================")
    codigoProducto = input("Ingrese el código del producto: ")
    for producto in lista_Producto:
        if producto.codigoProducto == codigoProducto:
            print("El código ya existe")
            RegistrarProducto()
            return
    nombreProducto = input("Ingrese el nombre del producto: ")
    descripcionProducto = input("Ingrese la descripción del producto: ")
    while True:
        precioProducto = input("Ingrese el precio del producto: ")
        try:
            precioProducto = float(precioProducto)
            break
        except:
            print("El precio debe ser un número")

    producto = Producto(codigoProducto, nombreProducto, descripcionProducto, precioProducto)
    lista_Producto.append(producto)

    print("Producto registrado con exito")
    print("================================")
    print("1. Registrar otro Producto      ")
    print("2. Regresar al menú principal   ")
    print("================================")
    opcion = input("Seleccione una opción a realizar  ")
    if opcion == "1":
        RegistrarProducto()
    elif opcion == "2":
        main()
    else:
        print("opcion invalida")
        main()
    main()


def RegistrarCliente():
    print("================================")
    print("       Registrar Cliente        ")
    print("================================")
    while True:
        try:
            nitCliente = int(input("Ingrese el NIT del cliente: "))
            break
        except: ValueError
        print("El NIT debe ser un número")
    for cliente in lista_Cliente:
        if cliente.nitCliente == nitCliente:
            print("El NIT ya existe")
            RegistrarCliente()
            return
    nombreCliente = input("Ingrese el nombre del cliente: ")
    correoCliente = input("Ingrese el correo del cliente: ")
    
    cliente = Cliente(nombreCliente, correoCliente, nitCliente)
    lista_Cliente.append(cliente)

    print("Cliente registrado con exito")
    print("================================")
    print("1. Registrar otro Cliente       ")
    print("2. Regresar al menú principal   ")
    print("================================")
    opcion = input("Seleccione una opción a realizar  ")
    if opcion == "1":
        RegistrarCliente()
    elif opcion == "2":
        main()
    else:
        print("opcion invalida")
        main()
    
main()
