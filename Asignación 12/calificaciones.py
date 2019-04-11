import statistics

def leeCalifs():
    califs = []
    numAlumnos = int(input("Ingrese el numero de alumnos "))
    count = 0
    while(count<numAlumnos):
        califs.append(int(input("Ingrese el promedio del alumno " + str(count+1)+ " ")))
        count+=1
    
    return califs

def mediaDevest(califs):
    media = statistics.mean(califs)
    devEst = statistics.stdev(califs)
    stats = (media,devEst)
    return stats

def generaCalifsLetra(califs,stats):
    califsLetra = []    
    for x in califs:
        califsLetra.append(obtenCalifLetra(x,stats))
    
    return califsLetra
        

def obtenCalifLetra(calif, stats):
    mediaCalif = stats[0]
    sCalif = stats[1]

    if  mediaCalif + sCalif <= calif :
        return 'A'
    elif mediaCalif + 0.5*sCalif <= calif < mediaCalif + sCalif:
        return 'B'
    elif mediaCalif - 0.5*sCalif <= calif < mediaCalif + 0.5*sCalif:
        return 'C'
    elif mediaCalif - sCalif <= calif < mediaCalif - 0.5*sCalif:
        return 'D'
    elif calif < mediaCalif - sCalif:
        return 'F'

def listaCalifs(numeros, letras):
    contador = 0
    for x in numeros:        
        print("Calificacion del alumno " + str(contador+1) + ": " + str(numeros[contador]) + " " + str(letras[contador]))
        contador = contador + 1


califs = leeCalifs()
stats = mediaDevest(califs)
letras = generaCalifsLetra(califs,stats)
listaCalifs(califs,letras)