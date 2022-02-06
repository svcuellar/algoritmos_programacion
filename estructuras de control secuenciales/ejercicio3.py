"""
entradas
sueldobase-->s-->float
totalventauno-->v_1-->float
totalventados-->v_2-->float
totalventatres-->v_3-->float

salidas
totalcomisiones-->com-->float
sueldototal-->t-->float
"""

#entradas
s=float(input("Ingrese el sueldo base: "))

v_1=float(input("Ingrese la venta uno: "))
v_2=float(input("Ingrese la venta dos: "))
v_3=float(input("Ingrese la venta tres: "))

#caja negra
com=round((v_1+v_2+v_3)*0.10, 2)
t=round((s+com), 2)

#salidas
print("El total por comisiones es: ", com)
print("El sueldo total es: ", t)