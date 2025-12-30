def validar_cedula(cedula):
    # Verificar que la cédula tenga 10 dígitos
    if len(cedula) != 10 or not cedula.isdigit():
        return False

    # Los dos primeros dígitos corresponden a la provincia (01-24), más el "30" de los extranjeros
    provincia = int(cedula[:2])
    if not (1 <= provincia <= 24 or provincia == 30):
        return False

    # El tercer dígito debe estar en el rango de 0 a 6 para cédulas válidas
    tercer_digito = int(cedula[2])
    if tercer_digito >= 6:
        return False

    # Coeficientes para la validación
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]

    # Aplicar el algoritmo de validación
    suma = 0
    for i in range(9):
        valor = int(cedula[i]) * coeficientes[i]
        if valor >= 10:
            valor -= 9
        suma += valor

    # Obtener el dígito verificador
    digito_verificador = 10 - (suma % 10)
    if digito_verificador == 10:
        digito_verificador = 0

    # Comparar el dígito verificador con el último dígito de la cédula
    return digito_verificador == int(cedula[9])