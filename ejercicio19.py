'''
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
'''


def det_bisiesto(datoint):
    if (datoint % 4 == 0 and datoint % 100 or datoint % 400 == 0):
      return True
    return False

datoint = int(input("Introduce un año para saber si fue o sera bisiesto: "))

if det_bisiesto(datoint):
  print(f"{datoint} es bisiesto")
else:
  print(f"{datoint} no es bisiesto")
