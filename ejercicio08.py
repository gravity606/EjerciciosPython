'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

print("En esta aplicacion puede averiguar su indice de masa corporal")
print(" ")
print("Para ello, introduzca los datos que le solicitamos")

peso_kg = float(input(f"Introduzca su peso en kg: "))
altura_m = float(input(f"A continuacion, introduzca su altura en metros: ")) 

IMC = peso_kg / altura_m**2

print(f"Su indice de mas corporal es de: {IMC}")

if IMC < 18.5:
    print("Debes engordar")
elif IMC >25:
    print("Debes adelgazar")
else:
    print("Tu indice de masa corporal es bueno")
    