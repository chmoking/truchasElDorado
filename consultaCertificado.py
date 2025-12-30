def consultaCertificado(numero_certificado):
    certificados = {
        "id":[1,2,3,4,5],
        "nombre":[ "Juan Perez", "Maria Gomez", "Carlos Ruiz", "Ana Torres", "Luis Fernandez"],
        "curso":["Python Básico", "Data Science", "Desarrollo Web", "Machine Learning", "Bases de Datos"]
    }
    #"select * from certificados where id = numero_certificado"
    if numero_certificado in certificados["id"]:
        indice = certificados["id"].index(numero_certificado)
        return f"Certificado válido para: {certificados['nombre'][indice]} - Curso: {certificados['curso'][indice]}"
    else:
        return "Certificado no válido"

def main():
    print("-----Consulta de Certificados-----")
    print("""
          1. Iniciar como administrador
          2. Consultar certificado
          3. Salir""")
    opcion = input("Seleccione una opción: ")
    while opcion == "2":
        try:
            numero_certificado = int(input("Ingrese el número de certificado: "))
            resultado = consultaCertificado(numero_certificado)
            print(resultado)
        except ValueError:
            print("ERROR: Por favor, ingrese un número válido.")

main()