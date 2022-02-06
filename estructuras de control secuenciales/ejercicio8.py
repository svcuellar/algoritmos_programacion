"""
entradas
longituda-->a-->float
longitudb-->b-->float
longitudc-->c-->float

salidas
areatriangulo-->area-->float
"""

#entradas
a=float(input("Longitud del lado a: "))
b=float(input("Longitud del lado b: "))
c=float(input("Longitud del lado c: "))

#caja negra
s=(a+b+c)/2

area=round((s*(s - a)*(s - b)*(s - c))**(1 / 2), 2)

#salidas
print("El area del triangulo es", area)