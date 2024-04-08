'''
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''

def  conversor_milkil(mil):
    km = mil * 1.60934
    return km

millas = float(input("Introduce el numero de millas que deseas convertir a kilometros: "))
kilometros = conversor_milkil(millas)

print(f"{millas} millas es igual a {kilometros} kilometros")