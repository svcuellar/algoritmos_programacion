"""
entradas
cantidadmetros-->m-->float

salidas
metrosapulgadas-->pu-->float
mmetrosapies-->pi-->float
"""

#entradas
m=float(input("Ingrese la cantidad de metros: "))

#caja negra
pu=round((m*39.27), 2)
pi=round((pu/12), 2)

#salidas
print(m, " metros equivalen a ", pu, " pulgadas y ", pi, " pies")