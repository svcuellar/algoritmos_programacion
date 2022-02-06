"""
entradas
notaexamenmatematicas-->exa_m-->float
notatarea1matematicas-->t1_m-->float
notatarea2matematicas-->t2_m-->float
notatarea3matematicas-->t3_m-->float

notaexamenfisica-->exa_f-->float
notatarea1fisica-->t1_f-->float
notatarea2fisica-->t2_f-->float

notaexamenquimica-->exa_q-->float
notatarea1quimica-->t1_q-->float
notatarea2quimica-->t2_q-->float
notatarea3quimica-->t3_q-->float

salidas
promediomatematicas-->prom_m-->float
promediofisica-->prom_f-->float
promedioquimica-->prom_q-->float
promediogeneral-->prom_g-->float
"""
#entradas
exa_m=float(input("Ingrese el examen de matematicas: ")) #notas matematicas
t1_m=float(input("Ingrese la tarea 1 de matematicas: "))
t2_m=float(input("Ingrese la tarea 2 de matematicas: "))
t3_m=float(input("Ingrese la tarea 3 de matematicas: "))

exa_f=float(input("Ingrese el examen de fisica: ")) #notas fisica
t1_f=float(input("Ingrese la tarea 1 de fisica: "))
t2_f=float(input("Ingrese la tarea 2 de fisica: "))

exa_q=float(input("Ingrese el examen de quimica: ")) #notas quimica
t1_q=float(input("Ingrese la tarea 1 de quimica: "))
t2_q=float(input("Ingrese la tarea 2 de quimica: "))
t3_q=float(input("Ingrese la tarea 3 de quimica: "))


#caja negra
prom_tm=(t1_m+t2_m+t3_m)/3  
prom_m=round(((exa_m*0.90)+(prom_tm*0.10)), 2) #promedios notas matematicas

prom_tf=(t1_f+t2_f)/2     
prom_f=round(((exa_f*0.80)+(prom_tf*0.20)), 2) #promedios notas fisica

prom_tq=(t1_q+t2_q+t3_q)/3  
prom_q=round(((exa_q*0.90)+(prom_tq*0.10)), 2) #promedios notas quimica

prom_g=round(((prom_m+prom_f+prom_q)/3), 2) #promedio general


#salidas
print("El promedio de matematicas es de ",prom_m)
print("El promedio de fisica es de ",prom_f)
print("El promedio de quimica es de ",prom_q)

print("El promedio general de las tres materias es de ",prom_g)