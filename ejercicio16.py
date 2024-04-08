'''
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''

def contador_parimpar(numeros):
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    return pares, impares

numeros = list(map(int, input("Intoruce una lista de numeros separados por espacios para saber cuantos son pares y cuantos son impares: ").split()))

pares, impares = contador_parimpar(numeros)
print(f"Entre los numeros introducidos hay un total de {pares} numero/s pares y {impares} numero/s impares")