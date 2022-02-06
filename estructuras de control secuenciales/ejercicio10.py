"""
entradas
cantidadchelinesaustriacos-->c-->float
cantidaddragmasgriegos-->dg-->float
cantidadpesetas-->p-->float

salidas
chelines_a_pesetas-->c_p-->float
dragmas_a_francosfrancese-->dg_ff-->float
pesetas_a_dolares-->p_d-->float
pesetas_a_lirasitalianas-->p_li-->float
"""

#entradas
c=float(input("Ingrese la cantidad de chelines austriacos "))
dg=float(input("Ingrese la cantidad de dragmas griegos "))
p=float(input("Ingrese la cantidad de pesetas "))

#caja negra
c_p=round((c*9.57), 2)
dg_ff=round(((c*0.957)/20.110), 2)
p_d=round((p/122.499), 2)
p_li=round((p/0.092289), 2)

#salidas
print(c, " chelines equivalen a", c_p, " pesetas")
print(dg, " dragmas griegos equivalen a", dg_ff, " francos franceses")
print(p, " pesetas equivalen a", p_d, " dolares y ", p_li, " liras italianas")