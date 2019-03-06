# Jesús Eduardo Ramírez Cota - 165732
# Programa que imprime los años bisiestos entre dos años dados.

def leeAnhos():
    anios = list()
    anios.append(int(input("Indique el primer año: ")))
    anios.append(int(input("Indique el segundo año: ")))
    return anios

def listaBisiestos(añoIni, añoFin):
    print("Años bisiestos entre "+ str(añoIni)+" y " + str(añoFin)+" :")
    while añoIni<=añoFin :
        if esBisiesto(añoIni) : print(str(añoIni)) 
        añoIni+=1

def  esBisiesto(añoN):
    # Si el año es divisible entre 4
    if añoN%4 == 0:
        # Si el año es divisible entre 100
        if añoN%100 == 0 :
            # Si el año es divisible entre 400
            if añoN%400 == 0 : return True
         # Si es divisible entre 4 pero no entre 100
        else:  return True
    else : return False


# Código principal.
años = leeAnhos()
listaBisiestos(años[0], años[1])


