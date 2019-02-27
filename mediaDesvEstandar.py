# Jesús Eduardo Ramírez Cota - 165732
# Programa que calcula el promedio de calificaciones de un grupo y su desviación estándar.



nAlumnos = 0
contador = 0
totalCalif = 0.0
promedio = 0.0
desviacion = 0.0
listaAlumnos = list()
nAlumnos = int(input("Indique el número de alumnos: "))

while(contador<nAlumnos) : 
    calificacion = float(input("Calificación del alumno "+ str(contador+1)+" : "))
    totalCalif+=calificacion
    listaAlumnos.append(calificacion)
    contador +=1
promedio = totalCalif/nAlumnos
print("Promedio = "+str(round(promedio, 2)))
contador=0
sumatoria = 0.0
while contador<len(listaAlumnos) :
    sumatoria+=((listaAlumnos[contador]-promedio)**2)
    contador+=1
desviacion=float((sumatoria/nAlumnos)**0.5)
print("Desviación estándar: "+str(round(desviacion, 2)))