cant_numeros = 3
num_usuario = 0
suma = 0
promedio = 0
for i in range(cant_numeros):
    num_usuario = int(input("ingrese un numero entero: "))
    suma += num_usuario
promedio = suma / cant_numeros
print(f"el promedio es: {promedio}")