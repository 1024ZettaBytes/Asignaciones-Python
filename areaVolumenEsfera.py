# Jesús Eduardo Ramírez Cota - 165732
# Programa que calcula el area y volumen de una esfera a partir de su radio
import math
# Se indica la medida del radio de la esfera
radio = input("Indique la medida del radio:")

# Se clacula el area
area = 4*math.pi*(float(radio)**2)

# Se calcula el volumen
volumen = (4/3)*math.pi*(float(radio)**3)

# Se imprimen los valores
print (round(area, 6))
print (round(volumen, 6))