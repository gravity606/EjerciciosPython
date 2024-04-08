'''
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''

# Grados Fahrenheit = (grados centígrados × 9/5) +32

def conversor_celsius_farenheit(grados):
    return grados * 9/5 + 32
  
grados_celsius = float(input("Porfavor, introduzca los grados celsius que desea convertir a grados farenheit: "))
grados_farenheit = conversor_celsius_farenheit(grados_celsius)
print(f"La temperatura en grados celsius que ha introducido, equivale a {grados_farenheit} grados farenheit")
