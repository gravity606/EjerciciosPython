'''
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''

print('Bienvenido al conversor de euros a dolores de su banco "ThePower"')
print("Cuanto euros desea convertir a dolares?")
euro = float(input("Introduzca la cantidad: "))
dolar = euro * 0.85
print(f"Acaba de recibir {dolar} dolares en el saldo de su cuenta")
print(" ")
print("Gracias por usar nuestro servicio.")
