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
        self.compra = []
    
    def agregarCompra(self, compra):
        self.compra.append(compra)
lista_Cliente = []



class Compra:
    contador_facturas = 0 
    
    def __init__(self, productos, cliente, costo_total):
        Compra.contador_facturas += 1
        self.id_compra = Compra.contador_facturas
        self.productos = productos
        self.cliente = cliente
        self.costo_total = costo_total
        self.impuesto = costo_total * 0.12 



      

lista_compra = []


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
    elif opcion == "3":
        RealizarCompra()
    elif opcion == "4":
        reporteCompra()
    elif opcion == "5":
        print("==============================")
        print("    Datos del Estudiante       ")
        print(" Estuardo Josué Vaquiax Reyes ")
        print("          202201336           ")
        print("==============================")
        main()
    elif opcion == "6":
        #os.system('clear')
        print("Gracias por usar el sistema")
        exit()
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

def RealizarCompra():
    print("================================")
    print("       Realizar Compra           ")
    print("================================")

 
    if len(lista_Producto) == 0:
        print("No hay productos registrados")
        main()
        return

 
    if len(lista_Cliente) == 0:
        print("No hay clientes registrados")
        main()
        return


    while True:
        nitCliente = int(input("Ingrese el NIT del cliente: "))
        cliente = None
        for c in lista_Cliente:
            if c.nitCliente == nitCliente:
                cliente = c
                break
        if cliente is None:
            print("NIT de cliente no existe")
        else:
            break

   
    productos_compra = []

   
    while True:
        print("\nSubmenú:")
        print("1. Agregar Producto")
        print("2. Terminar Compra y Generar Factura")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nLista de productos disponibles:")
            for producto in lista_Producto:
                print(f"{producto.codigoProducto} - {producto.nombreProducto} - {producto.precioProducto}")

       
            codigoProducto = input("Ingrese el código del producto: ")
            producto = None
            for p in lista_Producto:
                if p.codigoProducto == codigoProducto:
                    producto = p
                    break
            if producto is None:
                print("Código de producto no existe")
            else:
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad: "))
                        if cantidad <= 0:
                            print("La cantidad debe ser mayor que cero")
                        else:
                            break
                    except ValueError:
                        print("La cantidad debe ser un número entero positivo")

                productos_compra.append((producto, cantidad))

                print(f"Producto '{producto.nombreProducto}' agregado correctamente.")

        elif opcion == "2":
            if not productos_compra:
                print("No hay productos en la compra.")
                break  

          
            costo_total_compra = sum(producto.precioProducto * cantidad for producto, cantidad in productos_compra)
            
            impuesto = costo_total_compra * 0.12

           
            compra = Compra(productos_compra, cliente, costo_total_compra)
            lista_compra.append(compra)

            print("\nCompra realizada con éxito.")
            print(f"Costo total: {costo_total_compra}")
            print(f"Impuesto: {impuesto}")
            print(f"Costo total con impuesto: {costo_total_compra + impuesto}")
            print("Factura generada.")

            main()

        else:
            print("Opción inválida")


def reporteCompra():
    print("================================")
    print("      Reporte de Compra         ")
    print("================================")

    if len(lista_compra) == 0:
        print("No hay compras registradas")
        main()
        return

    print("IDs de compras disponibles:")
    for compra in lista_compra:
        print(compra.id_compra)

    while True:
        try:
            id_compra = int(input("Ingrese el ID de la compra: "))
            compra_seleccionada = next((compra for compra in lista_compra if compra.id_compra == id_compra), None)
            if compra_seleccionada is None:
                print("El ID de compra no existe")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido para el ID de compra")


    print("\nDetalles de la compra:")
    print(f"ID de Compra: {compra_seleccionada.id_compra}")
    print(f"Cliente: {compra_seleccionada.cliente.nombreCliente} - NIT: {compra_seleccionada.cliente.nitCliente}")
    print("Productos comprados:")
    for producto, cantidad in compra_seleccionada.productos:
        print(f"{producto.nombreProducto} - Cantidad: {cantidad}")
    print(f"Costo total: {compra_seleccionada.costo_total}")
    print(f"Impuesto: {compra_seleccionada.impuesto}")
    print(f"Costo total con impuesto: {compra_seleccionada.costo_total + compra_seleccionada.impuesto}")
    print("================================")
    print(" seleccione una opción a realizar  ")
    print("1. Regresar al menú principal   ")
    print("2. consultar otra compra       ")
    print("================================")

    opcion = input("Seleccione una opción a realizar  ")
    if opcion == "1":
        main()
    elif opcion == "2":
        reporteCompra()
    else:
        print("opcion invalida")
        main()

    
main()
