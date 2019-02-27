# Jesús Eduardo Ramírez Cota - 165732
# Programa que indica si un año ingresado es bisiesto o no.


# Se indica el año
año=0
año = input("Indique el año: ")
 # Si el año es divisible entre 4
if int(año)%4==0:
     # Si el año es divisible entre 100
    if int(año)%100==0:
        # Si el año es divisible entre 400
        if int(año)%400==0 :   
            print("Sí es bisiesto.") 
        # Si es divisible entre 100 pero no entre 400
        else : print("No es bisisesto.")
    # Si es divisible entre 4 pero no entre 100
    else: print("Si es bisiesto.")
# Si no es divisible entre 4
else :
     print("No es bisiesto")