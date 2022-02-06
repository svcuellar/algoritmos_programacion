"""
entradas
parcial 1-->float-->cal1
parcial 2-->float-->cal2
parcial 3-->float-->cal3
examen final-->float-->exa
trabajo final-->float-->trab    

salidas
nota definitiva-->float-->nota
"""

#entradas
cal1=float(input("Calificacion parcial 1: "))
cal2=float(input("Calificacion parcial 2: "))
cal3=float(input("Calificacion parcial 3: "))
exa=float(input("Examen final: "))
trab=float(input("Trabajo final: "))

#caja negra
promp=(cal1+cal2+cal3)/3
nota=round((((promp*0.55)+(exa*0.33)+(trab*0.15))), 2)

#salidas
print("La calificacion final es: ",nota)