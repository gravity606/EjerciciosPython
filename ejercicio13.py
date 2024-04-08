'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''

#Numero primo, mayor que 1, solo puede ser dividido por si mismo o por uno

#def num_primos(numero):
#    range(2,(numero - 1))

#numero = 11
#a = list(range(2,(numero)))
#print(a)

def es_primo(numero):
    if numero <= 1:
       return False
    for i in range(2, numero):
        if numero % 1 == 0:
          return False
    return True

numero = int(input("Intorduce un numero para comprobar si es primo: "))

if es_primo(numero):
    print("El numero introducido es primo")
else:
    print("El numero introducido no es primo")

