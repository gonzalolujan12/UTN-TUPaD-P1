def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


num = int(input("Ingresar numeros: ") )
print(suma_digitos(num))  
    