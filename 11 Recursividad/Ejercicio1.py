def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingrese un número entero: "))
if numero < 0:
    print("El número debe ser positivo o cero.")
else:
    print(f"El factorial de {numero} es {factorial(numero)}")