"""
entradas
mujeres-->muj-->int
hombres-->hom-->int


sumatotal=tot

salidas
porcentajemujeres=mujp
porcentajehombres=homp
"""

#entradas
muj=int(input("Ingrese el numero de mujeres "))
hom=int(input("Ingrese el numero de hombres "))

#caja negra
tot=muj+hom
mujp=(muj/tot)*100
homp=(hom/tot)*100

#salidas
print("El porcentajes de mujeres es ", mujp, "%")
print("El porcentajes de hombres es ", homp, "%")