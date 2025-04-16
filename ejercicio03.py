'''
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
'''


def detector_menores_sinceros(numero):
    if numero >= 18:
        return("Eres mayor de edad, espero que no estes mintiendo...")
    elif numero <= 0:
        return("Lamento comunicarte que aun no existes...")
    else:
        return("Gracias por ser sincero, eres menor de edad.")

print("Agradecemos la maxima sinceridad posible")
edad = int(input("Porfavor, introduce tu edad para poder comprobar si eres mayor de edad: "))
la_verdad = detector_menores_sinceros(edad)
print(la_verdad)
