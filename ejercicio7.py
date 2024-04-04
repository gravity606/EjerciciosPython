'''
Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.
'''

print("Bienvenido a: ")
print('"ThePower Calculator"')
print("Probablemente la calculadora mas potente del mercado")
print("Capaz de hacer operaciones simples con dos cifras")
print(" ")
print("Vamos a calcular!")
print(" ")

valor1 = int(input("Introduzca el primer numero: "))
valor2 = int(input("Introduzca el segundo numero: "))

print(" ")
print("Que desea hacer con ellos?")
print("(Introduce el numero de operacion y pulsa enter)")
print(" ")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print(" ")

operacion = float(input("Seleccion: "))

if operacion == 1:
    print(" ")
    print(f"Aqui tiene su operacion: ",valor1," + ",valor2," = ",valor1+valor2,"")
elif operacion == 2:
    print(" ")
    print(f"Aqui tiene su operacion: ",valor1," - ",valor2," = ",valor1-valor2,"")
elif operacion == 3:
    print(" ")
    print(f"Aqui tiene su operacion: ",valor1," x ",valor2," = ",valor1*valor2,"")
elif operacion == 4:
    print(" ")
    print(f"Aqui tiene su operacion: ",valor1," / ",valor2," = ",float(valor1/valor2),"")
else:
    print("Seleccion no valida, reinicia la aplicacion")

print(" ")
print("Gracias por utilizar nuestra calculadora.")
print(" ")