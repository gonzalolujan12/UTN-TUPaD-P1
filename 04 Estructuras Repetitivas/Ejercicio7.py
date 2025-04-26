suma = 0
numero = int(input("ingrese un numero entero positivo: "))
if numero > 0:
    for i in range(0, numero+1):
        suma += i
else:     
     print("debe ingresar un numero entero positivo..")
print(f"la suma de todos los numeros comprendidos entre 0 y {numero} es {suma} ")