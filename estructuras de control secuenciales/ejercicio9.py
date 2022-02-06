"""
entradas
horastrabajadas-->nh-->float
preciohora-->ph-->float

salidas
salarioneto-->th-->float
"""

#entradas
nh=float(input("Ingrese numero de horas trabajadas: "))
ph=float(input("Ingrese el precio de la hora: "))

#caja negra
th=(nh*ph)*0.80

#salidas
print("El salario neto es", th)