def menu():
    print("-----Menu Vendedor-----")
    print("""
          1. Gestionar Clientes
          2. Registrar Venta
          3. Cerrar Sesion""")
    opcion = input("Seleccione una opcion: ")
    while opcion != "3":
        if opcion == "1":
            gestionar_clientes()
        elif opcion == "2":
            registrar_venta()
        opcion = input("Seleccione una opcion: ")
    
def gestionar_clientes():
    print("Gestionando clientes...")

def registrar_venta():
    print("Registrando venta...")