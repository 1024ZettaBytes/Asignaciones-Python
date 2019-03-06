# Jesús Eduardo Ramírez Cota - 165732
# Programa que integra y tabula de acuerdo a la opción del menú seleccionada.

def menu() :
    print("I)ntegrar\nT)abular\nS)alir")
    opc = input("Seleccione una opción: ")
    return opc

def leeDatosIntegracion():
    valores = list()
    xi = float(input("Xi = "))
    xf = float(input("xf = "))
    nRectan = int(input("Número de rectángulos = "))
    valores.append(xi)
    valores.append(xf)
    valores.append(nRectan)
    return valores

def integrar(xi, xf, n):
    area = 0.0
    incremento = (xf-xi)/n
    print(str(incremento))
    x =xi+incremento
    while x<=xf :
        area += incremento*((x**3)-(2*x)+3) 
        x+=incremento
    return area

def leeDatosTabulación():
    valores = list()
    xi = float(input("Límite inferior = "))
    xf = float(input("Límite superior = "))
    nRectan = float(input("Incremento = "))
    valores.append(xi)
    valores.append(xf)
    valores.append(nRectan)
    return valores

def tabular(lInf, lSup, incremento):
    print("   X      Y   ")
    while lInf<=lSup :
        print(" "+str(round(lInf, 4))+"   "+str(round((lInf**3)-(2*lInf)+3, 4)))
        lInf+=incremento

# Código principal.
while(True) :
    opc = menu()
    if opc == "I" :
        valores = leeDatosIntegracion()
        integrar(valores[0], valores[1], valores[2])
    elif opc == "T" :
        valores = leeDatosTabulación()
        tabular(valores[0], valores[1], valores[2])
    elif opc == "S": break
    else: print("ERROR: No es una opción válida.\n")