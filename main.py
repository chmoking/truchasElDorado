import menuAdmin,menuGerente,menuVendedor
import hashlib, getpass,os,main2,recuperar

while True:
    os.system("cls")
    print("-----Sistema de Gestion-----")
    print("""
    Bienvenido al sistema de Ventas de Truchas 'El Dorado'
    1. Inicio de Sesion
    2. Recuperar Contraseña
    3. Salir
    """)
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        miUsuario = input("Ingrese su usuario: ")
        miPassword = getpass.getpass("Ingrese su contraseña: ")
        hashPass = hashlib.md5(miPassword.encode('utf-8')).hexdigest()
        resultado = main2.inicioSesion(miUsuario, hashPass)
        if resultado == False:
            print("Usuario o contraseña incorrectos")
        else:
            print(f"Bienvenido {resultado[4]} inicias sesion como {resultado[6]}")
            os.system("pause")
            rol = resultado[6]
            if rol == "administrador":
                menuAdmin.menu()
            elif rol == "gerente":
                menuGerente.menu()
            elif rol == "vendedor":
                menuVendedor.menu()
        os.system("pause")
    elif opcion == "2":
        recuperar.recuperarPassword()
    elif opcion == "3":
        print("Saliendo del sistema...")
        break