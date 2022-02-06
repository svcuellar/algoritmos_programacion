"""
entradas
totalcompra-->c-->float

salidas
totalcondescuento-->dest-->float
"""

#entradas
c=float(input("Ingrese el total de la compra "))

#caja negra
des=c*0.15
dest=round(c-des, 2)

#salidas
print("Debera pagar ", dest) 