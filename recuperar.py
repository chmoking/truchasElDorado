import getpass, hashlib, os, conexion
from mysql.connector import Error
def recuperarPassword():
    os.system("cls")
    print("-----Recuperar Contraseña-----")
    usuario = input("Ingrese su nombre de usuario: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    print("Recuperar Contraseña (Solo Vendedores)")
    while True:
        newPassword = getpass.getpass("Ingrese su nueva contraseña: ")
        confirmPassword = getpass.getpass("Confirme su nueva contraseña: ")
        if newPassword == confirmPassword:
            break
        else:
            print("Las contraseñas no coinciden. Intente nuevamente.")
    hashNewPassword = hashlib.md5(newPassword.encode('utf-8')).hexdigest()
    update = f"update users set password = '{hashNewPassword}' WHERE usuario = '{usuario}' AND nombres = '{nombre}' AND apellidos = '{apellido}' AND rol = 'vendedor';"
    print(update)
    os.system("pause")
    try:
        miConexion = conexion.conectar()
        cursor = miConexion.cursor()
        cursor.execute(update)
        miConexion.commit()
        if cursor.rowcount > 0:
            print("Contraseña actualizada exitosamente.")
        else:
            print("No se encontró un usuario con los datos proporcionados o no es un vendedor.")
        os.system("pause")
    except Error as e:
        print("Error de MySQL:", e)
        os.system("pause")
        return False