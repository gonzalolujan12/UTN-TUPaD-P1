import random

salida = True

numero_aleatorio = random.randint(0, 9)

numero_usuario = 0

contador_intentos = 0

while salida:
    numero_usuario = int(input("adivina el numero entre 0 y 9: "))

    if numero_usuario == numero_aleatorio:
        salida = False

        contador_intentos += 1
    else:
        contador_intentos += 1
        print("numero incorrecto..")
    
print(f" A4divinaste.. \ncantidad de intentos: {contador_intentos}")
    