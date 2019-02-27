# Jesús Eduardo Ramírez Cota - 165732
# Programa que calcula la cantidad de cajas de mosaicos necesarias.
tipo=0.0
nCajas=0
opcion=""

# Se ingresa la cantidad de metros cuadrados.
nMetros = input("Indique la cantidad de metros cuadrados: ")
# Se indica el tipo de mosaico a usar.
opcion = input("Indique el tipo de mosaico ('P' primera o 'S' segunda): ")

# Se valida que la opcion ingresada sea válida y se asigna la cantidad de mosaico usable sin desperdicio
if opcion == 'P' or opcion =='p': tipo =0.9
elif opcion == 'S' or opcion =='s' :tipo =0.85
else : print("No es una opcion válida.")

# Se calcula la cantidad de cajas de acuerdo a la cantidad de metros cuadrados.
nCajas = int(nMetros)/tipo
print("Número de cajas necesarias: " + str(round(nCajas, 2)))
