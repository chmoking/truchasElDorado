import hashlib, conexion,os
from mysql.connector import Error


def inicioSesion(usuario, password):
    try:
        miConexion = conexion.conectar()
        cursor = miConexion.cursor()
        cursor.execute(f"select * from users where usuario like '{usuario}' and password like'{password}';")
        #print(f"select * from users where usuario like '{usuario}' and password like'{password}';")
        #os.system("pause")
        resultado = cursor.fetchone()
        if resultado:
            print("Acceso concedido")
            #os.system("pause")
            return resultado
        else:
            print("Usuario o contraseña incorrectos")
            os.system("pause")
            return False
    except Error as e:
        print("Error de MySQL:", e)
        return False
