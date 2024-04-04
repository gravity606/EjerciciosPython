'''
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''

def propina(total):
    return total * 0.15
  
total_sin = float(input("Porfavor, introduzca el precio de los platos y le indicaremos el precio total a pagar desglosando la propina incluida: "))
total_con = propina(total_sin) + total_sin
print(total_con)
print(f"El total de su cuenta es de {total_con} euros")
print(f"Esto incluye una propina de {total_sin}")
print("Gracias por su visita.")