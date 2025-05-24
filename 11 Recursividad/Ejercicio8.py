def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


numero=int(input("Ingresar un numero:"))
digito=int(input("Ingresar el digito a contar:"))
print(contar_digito(numero, digito))