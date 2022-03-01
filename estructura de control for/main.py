archivo=open('c:\Users\usuario\Desktop\estructura de control for\paises.txt', 'r')
#Imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#Imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la letra M
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:  
  if(i[0]=="M"):
    lista.append(i)
print(len(lista))
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
print("Paises que empiezan por u: ")
lista_p=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista_p.append(i[r])
  a="".join(lista_p)
  paises.append(a)
  lista_p=[]
for i in paises:  
  if i[0]=="U":
    print(i)

print("\nCiudades que empiezan por u: ")
lista_c=[]
ciudad=[]
for i in archivo:
  a2=i.index(":")
  for r in range(a2+2,len(i)-1):
    lista_c.append(i[r])
  a2="".join(lista_c)
  ciudad.append(a2)
  lista_c=[]
for i in ciudad:  
  if(i[0]=="U"):
    print(i)
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
lista=[]
c=0
for i in archivo:
  lista.append(i)
  a="".join(lista)
  c+=1
print(len(lista))
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a[0]=="S" and a[1]=="i" and a[2]=="n"):
    b=a.index(":")
    lista=[]
    break
  lista=[]
for i in range(b+2,len(a)-1):
  lista.append(a[i])
a="".join(lista)
print(a)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]   
print(a)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:  
  if(i[0]=="E"):  
    print(i)
    lista.append(i)
print("Total ciudades que empiezan por E: ",len(lista))
"""
#Busque e imprima la capital de Colombia
"""
capital=[]
col_b="Colombia: Bogotá"
a=col_b.index(":")
t=len(col_b)
for i in range(a+1,t):
    capital.append(col_b[i])
b="".join(capital)
print(b)
"""
#Imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#Imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México\n"):
    break
  lista=[]   
print(c)
"""
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
"""
for paises in archivo:
  paises.remove=("Madagascar: rey julien")
  paises.insert=(149,"Madagascar: Antananarivo")
"""
#Agregue un país que no esté en la lista 
"""
with open('paises.txt', 'a') as archivo:
    archivo.write('\nButan: Timbu')
archivo.close()
"""
archivo.close()