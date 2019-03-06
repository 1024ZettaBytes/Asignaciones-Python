# Jesús Eduardo Ramírez Cota - 165732
# Programa que calcula y tabula las distancias de un proyectil de acuerdo a su ángulo de inclinación.


import math

distancia =0.0
anguloMáximo = 0
distanciaMax = 0.0
v0 = float(input("Indique la velocidad inicial: "))
print("Ángulo    Distancia")
for angulo in range(0, 91):
    if angulo == 0 or angulo%5 == 0:
            distancia = 2*(v0**2)*math.sin(angulo)*math.cos(angulo)/9.81
            if distancia>distanciaMax:
                    anguloMáximo=angulo
                    distanciaMax=distancia
            print("  "+str(round(angulo, 4))+"        "+str(round(distancia, 4)))
print("Ángulo para alcanzar la distancia máxima: "+str(round(anguloMáximo, 4))+", distancia máxima = "+str(round(distanciaMax, 4)))

        
