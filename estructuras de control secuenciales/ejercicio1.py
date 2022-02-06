"""
entradas
edadpersona1-->e_uno-->int
edadpersona2-->e_dos-->int
edadpersona3-->e_tres-->int

salidas
promedioedades-->prom-->int
"""

#entradas
e_uno=int(input("Ingrese la edad de la persona uno: "))
e_dos=int(input("Ingrese la edad de la persona dos: "))
e_tres=int(input("Ingrese la edad de la persona tres: "))

#caja negra
prom=(e_uno+e_dos+e_tres)/3 

#salidas
print("El promedio de las tres edades es: ", prom) 