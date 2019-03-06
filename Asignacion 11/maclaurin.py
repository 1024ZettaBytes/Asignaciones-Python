# Jesús Eduardo Ramírez Cota - 165732
# Módulo que contiene las funciones seno(x, n) y exp(x, n), se usando n término de la serie de Maclaurin.

import math
def seno(x, n):
    termino = 0
    seno = 0.0
    while termino < n:
        seno += ((-1)**termino)*(x**(2*termino + 1))/(math.factorial(2*termino + 1))
        termino+=1
    return seno

def exp(x, n):
    termino = 0
    expX = 0.0
    while termino < n:
        expX += (x**termino)/(math.factorial(termino))
        termino+=1
    return expX

def tabulaFuncion(f, x, nMin, nMax, incN):
    print("Tabla para la función "+str(f)+" con valores x = "+str(x)+", nMin = "+str(nMin)+", nmax = "+str(nMax)+", incN = "+str(incN))
    if f == "S":
        print("   x      n      seno(x, n)")
        while nMin <= nMax:
            print(str(x)+"  "+str(nMin)+"      "+str(seno(x, nMin)))
            nMin+=incN
    else :
        print("   x      n      exp(x, n)")
        while nMin <= nMax:
            print(str(x)+"  "+str(nMin)+"      "+str(exp(x, nMin)))
            nMin+=incN

# Código principal.

# Prueba de función seno(x, n)
def main():
    print("Prueba de función seno(x, n): x = 0.78539, n = 5, seno(0.78539, 5) = "+str(seno(0.78539, 5)))
    print("Prueba de función seno(x, n): x = 0.78539, n = 10, seno(0.78539, 10) = "+str(seno(0.78539, 10)))
    print("Prueba de función seno(x, n): x = 1.57079, n = 5, seno(1.57079, 5) = "+str(seno(1.57079, 5)))
    print("Prueba de función seno(x, n): x = 1.57079, n = 10, seno(1.57079, 10) = "+str(seno(1.57079, 10)))
    print("Prueba de función exp(x, n): x = 1.0, n = 5, exp(1.0, 5) = "+str(exp(1.0, 5)))
    print("Prueba de función exp(x, n): x = 1.0, n = 10, exp(1.0, 10) = "+str(exp(1.0, 10)))
    print("Prueba de función exp(x, n): x = -1.0, n = 5, exp(-1.0, 5) = "+str(exp(-1.0, 5)))
    print("Prueba de función exp(x, n): x = -1.0, n = 10, exp(-1.0, 10) = "+str(exp(-1.0, 10)))

    #Prueba de tabulación
    tabulaFuncion("S", 0.785398, 5, 10, 1)
    tabulaFuncion("S", 1.570796, 5, 15, 2)
    tabulaFuncion("E", 1.0, 5, 10, 1)
    tabulaFuncion("E", -1.0, 5, 15, 2)

# LLAMAR A LA FUNCION main() para realizar las pruebas