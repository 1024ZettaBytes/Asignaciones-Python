# Jesús Eduardo Ramírez Cota - 165732
# Programa que indica el número de billetes de cada nominación que se debe proporcionar al hacer un retiro


# Se indica la cantidad a retirar(multiplo de 50)
retiro=0
retiro = input("Indique la cantidad a retirar:")

 # Se calcula la cantidad de billetes
bMil = int(int(retiro)/1000)
retiro = int(retiro)%1000
bQuinientos = int(int(retiro)/500)
retiro = retiro%500
bCien = int(int(retiro)/100)
retiro = retiro%100
bCincuenta = int(int(retiro)/50)

 # Se muestran los valores
print ("Cantidad de billetes de $1000: " + str(bMil))
print ("Cantidad de billetes de $500: " + str(bQuinientos))
print ("Cantidad de billetes de $100: " + str(bCien))
print ("Cantidad de billetes de $50: " + str(bCincuenta))
