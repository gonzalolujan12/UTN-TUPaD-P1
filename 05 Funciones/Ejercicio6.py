def Tabla_Multiplicar(n):
    for x in range(10):
        multiplicacion= n*x
        print(f"{n} * {x}= ", multiplicacion )
num= int (input("Ingresar un numero:"))
Tabla_Multiplicar(num)