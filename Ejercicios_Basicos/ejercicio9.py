"""
Crear una lista de números enteros y devuelva dos listas ordenadas.
La primera con los números pares y la segunda con los números impares.
"""

numeros = [9, 8, 7, 6, 5, 4, 3, 2, 1]
numeros.sort()
pares = []
impares = []
for num in numeros:
    if num % 2 == 0: pares.append(num)
    else: impares.append(num)
print("Los numeros pares de la lista son:", pares)
print("Los numeros impares de la lista son:", impares)