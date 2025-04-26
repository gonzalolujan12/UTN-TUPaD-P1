nume= 0
suma = 0
salida = True

while salida:
    
    numero = int(input("ingrese un numero (0 para finalizar): "))

    if numero == 0:
        salida = False

    else:
        suma = suma + numero

print(f"la suma de los numeros ingresados es: {suma}")