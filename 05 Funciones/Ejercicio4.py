from math import pow,pi
def Calcular_perimetro(rad):
    per=2*pi*rad
    print(f"Perimetro:{per} ")
def Calcular_area(rad):
    area=pi*pow(rad,2)
    print(f"Area: {area}")


radio =float(input ("Ingresar el radio del circulo:") )
Calcular_perimetro(radio  )
Calcular_area(radio)