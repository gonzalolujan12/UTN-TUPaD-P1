def Conversion_unidades(Celsius):
    Formula=Celsius*9/5+32
    print (f"La cantidad de {Celsius} grados Celsius es {Formula} grados Franheit ")

Grados=float(input("Ingresar los grados:"))
Conversion_unidades(Grados)
