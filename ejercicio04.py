'''
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''

def contador_vocales(palabra):
    vocales = "AaEeIiOoUu"
    total_vocales = 0
    for letra in palabra:
        if letra in vocales:
            total_vocales += 1
    return total_vocales

palabra_introducida = input("Introduce una palabra y te dire cuantas vocales tiene: ")
vocales = contador_vocales(palabra_introducida)
print(f"Tu palabra tiene un total de {vocales} vocales.")
