'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
'''

def contador_palabras(palabrasint):
    palabras = palabrasint.split()
    num_palabras = len(palabras)
    return num_palabras

palabrasint = input("Escribe la cantidad de palabras que quieras: ")
num_palabras = contador_palabras(palabrasint)
print(f"Has introducido {num_palabras} palabras")