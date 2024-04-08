'''
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''

def calcular_edad(nacimiento):
      actual = 2024
      edadtotal = actual - nacimiento
      return edadtotal

nacimiento = int(input("Introduzca su año de nacimiento para averiguar su edad: "))
edad = calcular_edad(nacimiento)
print(f"Su edad es {edad}")
