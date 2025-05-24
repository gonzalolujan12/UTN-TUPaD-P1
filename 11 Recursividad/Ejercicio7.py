def contar_bloques(base):
    if base == 0:
       return 0
    else:
        return base + contar_bloques(base - 1)

base = 3
total_bloques = contar_bloques(base)
print(f"Para una pirámide con {base} Bloques de base, se necesitan {total_bloques} bloques en total.")