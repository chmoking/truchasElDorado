def login(user, password):
    #simular la base de datos de usuarios
    dicUsuarios={
    "admin":"7488e331b8b64e5794da3fa4eb10ad5d",
    "gerente":"gerente123",
    "vendedor":"vendedor123"
    }

    if user == "admin" and password == dicUsuarios["admin"]:
        return "admin"
    elif user == "gerente" and password == dicUsuarios["gerente"]:
        return "gerente"
    elif user == "vendedor" and password == dicUsuarios["vendedor"]:
        return "vendedor"
    else:
        return "error"