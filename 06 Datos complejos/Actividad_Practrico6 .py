1)# Diccionario original
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el diccionario actualizado
print(precios_frutas)

================================================================================

2)# Diccionario con las frutas ya agregadas (desde el punto anterior)
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario actualizado
print(precios_frutas)

================================================================================

3)# Diccionario actualizado con los nuevos precios
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Crear una lista solo con los nombres de las frutas
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista
print(lista_frutas)

==================================================================================

4)# Crear un diccionario vacío para los contactos
agenda = {}

# Cargar 5 contactos
print("Cargá 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i + 1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

# Consultar un número por nombre
consulta = input("\nIngresá el nombre del contacto que querés buscar: ")

# Mostrar el número si existe
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"{consulta} no está en la agenda.")

============================================================================
# Solicitar una frase al usuario
frase = input("Ingresá una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# Contar la frecuencia de cada palabra usando un diccionario
frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Mostrar los resultados
print("\nPalabras únicas:")
print(palabras_unicas)

print("\nFrecuencia de cada palabra:")
print(frecuencia_palabras)
=============================================================================

# Diccionario para almacenar los alumnos y sus notas
alumnos = {}

# Ingreso de datos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
===========================================================================0

7)# Sets de estudiantes que aprobaron cada parcial
parcial1 = {'Ana', 'Luis', 'Carlos', 'Marta'}
parcial2 = {'Luis', 'Marta', 'Sofía', 'Pedro'}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Aprobaron ambos parciales:")
print(ambos)

print("\nAprobaron solo uno de los dos:")
print(solo_uno)

print("\nAprobaron al menos un parcial:")
print(al_menos_uno)

=============================================================================
8)# Diccionario inicial con productos y sus stocks
stock_productos = {
    'pan': 20,
    'leche': 15,
    'huevos': 30
}

# Mostrar el stock inicial
print("Stock inicial de productos:")
print(stock_productos)

# Solicitar producto al usuario
producto = input("\nIngresá el nombre del producto a consultar o modificar: ").lower()

# Consultar si el producto ya existe
if producto in stock_productos:
    print(f"\nStock actual de '{producto}': {stock_productos[producto]}")
    
    # Preguntar si se desea agregar unidades
    agregar = input("¿Querés agregar unidades a este producto? (sí/no): ").lower()
    if agregar == 'sí' or agregar == 'si':
        unidades = int(inpu
================================================================================
9)# Crear la agenda como un diccionario vacío
agenda = {}

# Cargar algunos eventos
for i in range(3):
    dia = input(f"Ingresá el día del evento {i + 1} (por ejemplo, 'Lunes'): ")
    hora = input(f"Ingresá la hora del evento {i + 1} (por ejemplo, '14:00'): ")
    evento = input(f"¿Qué evento tenés el {dia} a las {hora}?: ")
    
    # Guardar en la agenda usando una tupla como clave
    agenda[(dia, hora)] = evento

# Mostrar la agenda completa
print("\nAgenda completa:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

==================================================================================
10)# Diccionario original: países -> capitales
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Brasil': 'Brasilia',
    'Uruguay': 'Montevideo'
}

# Invertir el diccionario: capitales -> países
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el nuevo diccionario
print(capitales_paises)

