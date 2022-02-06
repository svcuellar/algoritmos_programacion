"""
entradas
nombretrabajador-->n-->str
numerohorasnormales-->hn-->float
preciohoranormal-->ph-->float
numerohorasextra-->he-->float
sueldobase-->sb-->float
numerohijos-->nh-->int

salidas
totalporasignaciones-->asig-->float
totalpordeducciones-->de-->float
salarioneto-->sn-->float
"""
#entradas
n=str(input("Ingrese el nombre del trabajador "))
hn=float(input("Ingrese el numero de horas normales trabajadas "))
ph=float(input("Ingrese el pago de una hora normal "))
he=float(input("Ingrese el numero de horas extras trabajadas "))
sb=float(input("Ingrese el sueldo base "))
nh=int(input("Ingrese el numero de hijos "))

#caja negra
phe=(ph*1.25)*he

pf=sb*0.05
ph=sb*0.02
ca=sb*0.07

de=pf+ph+ca

ac=250000
ph=180000
h=nh*173000

asig=ac+ph+h

sn=round((sb+phe+asig)-de, 2)

#salidas
print("Las asignaciones seran de ", asig)
print("Las deduciones seran de", de)
print("El salario neto sera de ", sn)