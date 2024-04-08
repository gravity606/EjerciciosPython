'''
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''

def convertir_horas_min(minutos):
    horas = minutos // 60
    minutos_rest = minutos % 60
    return horas, minutos_rest

minutos = int(input("Introduce un numero de minutos: ")) 
horas, minutos_rest = convertir_horas_min(minutos)
print(f'El tiempo seria {horas} horas y {minutos_rest} minutos.')