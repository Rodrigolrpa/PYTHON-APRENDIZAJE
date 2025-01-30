'''                  EJERCICIO NUMERO #89
COMPROBAR SI UNA PALABRA ES PALINDROMO USANDO LAMBDA'''

palindromo = lambda palabra : 'PALINDROMO' if palabra == palabra[::-1] else "NO ES PALINDROMO"

print(palindromo('ANA'))