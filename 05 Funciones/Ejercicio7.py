def Operaciones_basicas(x, y):
    Suma= x+y
    Resta= x-y
    Multi= x*y
    Div= x/y
    tupla=(Suma, Resta, Multi, Div)
    print (type(tupla))
    return tupla
Valor1=int(input("El Valor 1:   "))
Valor2=int(input("El Valor 2:   "))

Cal=Operaciones_basicas(Valor1, Valor2)
print(Cal)