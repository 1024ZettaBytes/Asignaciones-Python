# Jesús Eduardo Ramírez Cota - 165732
# Programa que imprime los años bisiestos entre dos años dados.


año = 0
año2 = 0
año = int(input("Indique el primer año: "))
año2 = int(input("Indique el segundo año: "))
print("Años bisiestos entre "+ str(año)+" y " + str(año2)+" :")
# Hasta que el año menor sea divisible entre 4
while(año%4!=0) : año+=1

while año<=año2 :
     # Si el año es divisible entre 100
    if año%100 == 0:
        # Si el año es divisible entre 400
        if año%400 == 0 :   
            print(str(año)) 
    # Si es divisible entre 4 pero no entre 100
    else:  print(str(año))
    año+=4 

