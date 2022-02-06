"""
entradas
cantidabilletes50000-->n1-->int
cantidabilletes20000-->n2-->int
cantidabilletes10000-->n3-->int
cantidabilletes5000-->n4-->int
cantidabilletes2000-->n5-->int
cantidabilletes1000-->n6-->int
cantidabilletes500-->n7-->int
cantidabilletes100-->n8-->int

salidas
totaldinerobanco-->total-->float
"""

#entradas
n1=int(input("Ingrese la cantidad de billetes de 50000 "))
n2=int(input("Ingrese la cantidad de billetes de 20000 "))
n3=int(input("Ingrese la cantidad de billetes de 10000 "))
n4=int(input("Ingrese la cantidad de billetes de 5000 "))
n5=int(input("Ingrese la cantidad de billetes de 2000 "))
n6=int(input("Ingrese la cantidad de billetes de 1000 "))
n7=int(input("Ingrese la cantidad de billetes de 500 "))
n8=int(input("Ingrese la cantidad de billetes de 100 "))

#caja negra
n1_tot=n1*50000
n2_tot=n2*20000
n3_tot=n3*10000
n4_tot=n4*5000
n5_tot=n5*2000
n6_tot=n6*1000
n7_tot=n7*500
n8_tot=n8*100

total=(n1_tot+n2_tot+n3_tot+n4_tot+n5_tot+n6_tot+n7_tot+n8_tot)


#salidas
print("El banco tiene un total de ",total)