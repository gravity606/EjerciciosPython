'''
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

def selector_dia(numero):
    dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    if numero >= 1 and numero <= 7:
        return dias_semana[numero-1]
    else:
        return ("Ese dia no existe")

numero = int(input("Intoduzca el dia de la semana: "))
dia_seleccionado = selector_dia(numero)
print(dia_seleccionado)
