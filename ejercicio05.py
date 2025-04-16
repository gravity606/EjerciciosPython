'''
Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''

total = 0

for numero in range(2, 101, 2):
    total += numero

print(f"La suma de todos los números pares del 1 al 100 es {total}")
