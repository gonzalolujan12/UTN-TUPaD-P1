def potencia(n, m):
  if m == 0:
    return 1
  else:
    return n * potencia(n, m-1)


resultado = potencia(2,3)
print(resultado)