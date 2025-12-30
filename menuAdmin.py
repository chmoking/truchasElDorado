import os, funcionesAdmin
def menu():
    while True:
        os.system("cls")
        print("***--- Menú de Administrador ---***")
        print("1. Gestion de Usuarios")
        print("2. Gestion de Lotes")
        print("3. Reportes")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            gestionUsuarios()
        elif opcion == "2":
            gestionLotes()
        elif opcion == "3":
            reportes()
        elif opcion == "4":
            os.system("cls")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            os.system("pause")

def gestionUsuarios():
    funcionesAdmin.gestionUsuarios()

def gestionLotes():
    print("Funcionalidad de Gestión de Lotes")
    os.system("pause")

def reportes():
    print("Funcionalidad de Reportes")
    os.system("pause")