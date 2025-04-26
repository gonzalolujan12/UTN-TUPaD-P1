numero = int(input("Ingrese un número: "))
numero_invertido = 0
num_absoluto = abs(numero)

while num_absoluto > 0:
    digito = num_absoluto % 10

    numero_invertido = numero_invertido * 10 + digito
    
    num_absoluto //= 10  

if numero < 0:
    numero_invertido *= -1

print(f"El número invertido es: {numero_invertido}")