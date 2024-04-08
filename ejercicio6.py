'''
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''

def invertir_palabra(palabra):
    reves = ""
    for letra in palabra:
        reves = letra + reves
    return(reves)

dato_introducido = (input("Introduce una palabra para comprobar si es un palindromo: "))
palabra_reves = invertir_palabra(dato_introducido)

def comprobar_igualdad(comprobacion):
    if comprobacion == palabra_reves:
        print("Es un palindromo")
    else:
        print("No es un palindromo")

comprobar_igualdad(dato_introducido)
