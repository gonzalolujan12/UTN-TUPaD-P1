cantidad_numeros = 100
num_usuario = 0
num_pares = 0
num_impares = 0
num_negativos = 0
num_positivos = 0

for i in range(cantidad_numeros):

    num_usuario = int(input("ingrese un numero: "))

    if num_usuario % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    
    if num_usuario > 0:
        num_positivos += 1
    else:
        num_negativos += 1

print(f"numeros pares: {num_pares}")
print(f"numeros impares: {num_impares}")
print(f"numeros positivos: {num_positivos}")
print(f"numeros negativos: {num_negativos}")