"""
entradas
contraseña-->c-->int

salidas
acceso permitido-->str
clave invalida-->str
"""
while True:
    c=int(input(""))  #entradas
    if(c==2002):
        print("Acesso permitido")  #salidas
        break
    else:
        print("Senha invalida")  #salidas