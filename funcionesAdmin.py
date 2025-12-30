import os, hashlib, conexion, validaciones
from tabulate import tabulate
def gestionUsuarios():
    while True:
        os. system("cls")
        print("Funcionalidad de Gestión de Usuarios")
        print("""
          1. Nuevo Usuario
          2. Listar Usuarios
          3. Modificar Usuario
          4. Eliminar Usuario
          5. Volver al Menú Principal""")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nuevoUsuario()
        elif opcion == "2":
            listarUsuarios()
        elif opcion == "3":
            modificarUsuario()
        elif opcion == "4":
            eliminarUsuario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
    
def nuevoUsuario():
    #Validamos cedula con la funcion que esta en validaciones.py
    while True:
        cedula = input("Ingrese la cédula del nuevo usuario: ")
        if validaciones.validar_cedula(cedula):
            break
        else:
            print("Cédula inválida. Intente de nuevo.")
    usuario = input("Ingrese el username del nuevo usuario: ")
    password = input("Ingrese la contraseña del nuevo usuario: ")
    hashPass = hashlib.md5(password.encode('utf-8')).hexdigest()
    #validamos que el nombre y apellido solo contengan letras
    while True:
        nombre = input("Ingrese el nombre del nuevo usuario: ")
        if nombre.isalpha():
            break
        else:
            print("El nombre solo debe contener letras. Intente de nuevo.")
    #validamos que el nombre y apellido solo contengan letras
    while True:
        apellido = input("Ingrese el apellido del nuevo usuario: ")
        if apellido.isalpha():
            break
        else:
            print("El apellido solo debe contener letras. Intente de nuevo.")
    #validamos que el rol sea administrador, gerente o vendedor
    while True:
        print("""Ingrese el rol del nuevo usuario 
              1. administrador
              2. gerente
              3. vendedor): """)
        rol = input("Ingrese el rol del nuevo usuario (1/2/3): ")
        if rol == "1":
            rol = "administrador"
            break
        elif rol == "2":
            rol = "gerente"
            break
        elif rol == "3":
            rol = "vendedor"
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    insert=f"insert into users (cedula, usuario, password, nombres, apellidos, rol) values ('{cedula}', '{usuario}', '{hashPass}', '{nombre}', '{apellido}', '{rol}');"
    conexionBD = conexion.conectar()
    cursor = conexionBD.cursor()
    cursor.execute(insert)
    conexionBD.commit()
    conexionBD.close()
    os.system("pause")

def listarUsuarios():
    conexionBD = conexion.conectar()
    cursor = conexionBD.cursor()
    cursor.execute("select id, cedula, usuario, nombres, apellidos, rol from users;")
    resultados = cursor.fetchall()
    headers = ["ID", "Cédula", "Usuario", "Nombres", "Apellidos", "Rol"]
    print(resultados)
    print(tabulate(resultados, headers, tablefmt="psql"))
    conexionBD.close()
    os.system("pause")

def modificarUsuario():
    print("Funcionalidad de Modificar Usuario")
    os.system("pause")

def eliminarUsuario():
    print("Funcionalidad de Eliminar Usuario")
    os.system("pause")
