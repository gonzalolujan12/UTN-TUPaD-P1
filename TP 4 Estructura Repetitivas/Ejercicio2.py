numero = int(input("ingrese un numero entero: "))
digito = 0
while numero > 0:
    numero = numero // 10
    digito += 1
print(digito)