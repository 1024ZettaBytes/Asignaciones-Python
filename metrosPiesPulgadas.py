# Jesús Eduardo Ramírez Cota - 165732
# Programa que convierte una medida en metros a pies y pulgadas

# Se indica la medida en metros
metros = input("Indique la medida en metros:")

# Se convierte a pies
pies = float(metros)*3.28084

# Se convierte a pulgadas
pulgadas = float(metros)*39.3701

# Se imprimen los valores
print (round(pies, 4))
print (round(pulgadas, 4))