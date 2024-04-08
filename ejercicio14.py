'''
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''

def descuento(precio):
    desc = precio * 0.2
    pdesc = precio - desc
    return pdesc

precio_sind = float(input("Introduce el precio del producto a realizar descuento: "))
precio_cond = descuento(precio_sind)
print(f"El precio del articulo con un 20% de descuento es de {precio_cond}")