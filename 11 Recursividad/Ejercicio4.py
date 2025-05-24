def decimal_a_binario_recursivo(numero):
     if numero < 2:
          return str(numero)
     else:
           return decimal_a_binario_recursivo(numero // 2) + str(numero % 2)

numero_decimal= 10

numero_binario = decimal_a_binario_recursivo(numero_decimal)
print(f"El número {numero_decimal} en binario es: {numero_binario}")