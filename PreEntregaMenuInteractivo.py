# Lista de productos y stock de producto
productos = ["lavandina", "detergente", "jabon"]
stockProductos = [4, 8, 9]

# variable que unicia menu
opcion = -1

while opcion != 0:
    print("\n============== MENÚ ==============")
    print("==                              ==")
    print("==    1. Agregar producto       ==")
    print("==    2. Mostrar inventario     ==")
    print("==    0. Salir                  ==")
    print("==================================")

    opcion = int(input("Ingrese un número: "))

    # Agregar un producto
    if opcion == 1:
        print("\n============= AGREGAR PRODUCTO =============")
        agregarProducto = input("Ingrese el nombre del producto: ")
        agregarStock = int(input("Ingrese la cantidad del producto: "))

        # Agregar el producto y su stock a las listas
        productos.append(agregarProducto)
        stockProductos.append(agregarStock)

        print(f"Producto '{agregarProducto}' agregado con éxito.")

    # Mostrar el inventario de productos
    elif opcion == 2:
        print("\n============= INVENTARIO =============")
        if productos:
            for i in range(len(productos)):
                print(f"{productos[i]}: {stockProductos[i]} unidades")
        else:
            print("No hay productos en el inventario.")

    # Salir del menú
    elif opcion == 0:
        print("Vuelva pronto.")
        print("Visitame Youtube,com/@eze_gz")

    # Opción incorrecta
    else:
        print("Opción incorrecta. Intente de nuevo.")
