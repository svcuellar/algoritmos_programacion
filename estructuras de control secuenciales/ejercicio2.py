"""
entradas
capitalinvertido-->c_in-->float

salidas
ganancias-->g-->float
dinerototal-->t-->float
"""

#entradas
c_in=float(input("Ingrese la cantidad de capital invertido: "))

#caja negra
g=round(c_in*0.02, 2)
t=round(g+c_in, 2)

#salidas
print("La ganancia sera de ", g, " para un total de ", t)