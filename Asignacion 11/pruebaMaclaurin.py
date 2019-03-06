# Jesús Eduardo Ramírez Cota - 165732
# Programa que utiliza el módulo creado maclaurin.py y realiza pruebas con los datos ingresados por el usuario.
from maclaurin import tabulaFuncion
while True:
    opc = input("Indique la función que desea tabular S)eno o E)xponencial: ")
    if opc == "S" or opc == "E":
        x = float(input("x = "))
        nMin = float(input("nMin = "))
        nMax = float(input("nMax = "))
        incN = float(input("incN = "))
        tabulaFuncion(opc, x, nMin, nMax, incN)
        opc = opc = input("Desea repetir el cálculo ('S', 'N'): ")
        if opc != "S":
            break
    else : print("ERROR: No es una opción válida.")
        
