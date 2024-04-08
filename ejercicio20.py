'''
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''

def sumar_numeros(listanum):
    suma = 0
    for numero in listanum:
      suma += numero
    return suma

listanum = list(map(int, input("Introduce una lista de numeros separados por espacios para sumarlos: ").split()))
resultado = sumar_numeros(listanum)
print(f"El resultado de la suma de los numeros introducidos es: {resultado}")
