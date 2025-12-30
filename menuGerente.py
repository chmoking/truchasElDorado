def menu():
    print("-----Menu Gerente-----")
    print("""
    1. Stock de Productos
    2. Reportes de Ventas
    3. Cerrar Sesion
    """)
    opcion = input("Seleccione una opcion: ")
    while opcion != "3":
           if opcion == "1":
               stock_productos()
           elif opcion == "2":
               reportes_ventas()

def stock_productos():
        print("Mostrando stock de productos...")

def reportes_ventas():
        print("Mostrando reportes de ventas...")