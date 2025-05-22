def Saludar(nom,ape, ed, resi):
        print(f"Hola soy {nom} {ape} terngo {ed} y vivo en {resi}")

nombre=input("Ingresar su nombre:")
apellido=input ("Ingresar su apellido:")
edad= int(input("Ingresar su edad:"))
residencia=input("Ingresar su residencia:")
Saludar(nombre,apellido, edad, residencia)