def palindromo(palabra):
    if len(palabra) <= 1:
       return True
    else:
      if palabra[0] != palabra[-1]:
         return False
      else:
         return palindromo(palabra[1:-1])  
      
palabra= input ("Ingresar una palabra: " )
print(f"La palabra: {palabra } y es: {palindromo(palabra)}")