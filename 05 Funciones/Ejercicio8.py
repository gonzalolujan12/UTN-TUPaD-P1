from math import pow
def Calcular_IMC(Masa, Altura):
    IMC= Masa/pow(Altura, 2)
    print(f"El imc es:  {IMC}")

Masa=float(input("Ingresar su peso:"))
Altura=float(input("Ingresar su altura:"))
Calcular_IMC(Masa, Altura)
