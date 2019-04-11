#Programa para registrar y obtener información estadística sobre las alturas de los alumnos de un grupo.
#Jesús Eduardo Ramírez Cota 00000165732
import math
print("Programa para registrar y obtener información estadística sobre las alturas de los alumnos de un grupo.\n")

def leeDatos():
	listaAlumnos=[]
	nAlumno=1
	while True:
		matricula=int(input("Introduzca la matricula del alumno "+str(nAlumno)+" (0 para terminar): "))
		if(matricula==0):
			return listaAlumnos
		altura=float(input("Introduzca la altura del alumno: "))
		listaAlumnos.append((matricula,altura))
		nAlumno+=1
	return listaAlumnos

def despliegaDatos(listaAlumnos):
	print("| Matrícula | Altura |")
	print("--------------------")
	for matricula,altura in listaAlumnos:
		print("|   "+str(matricula)+"   |   "+str(altura)+"   |")
	print("--------------------")

def ordSeleccion(listaAlumnos,datoMenor):
	for x in range (len(listaAlumnos)-1):
		menor=x
		for y in range(x+1,len(listaAlumnos)):
			if datoMenor(listaAlumnos[y],listaAlumnos[menor]):
				menor=y
		if menor!=x:
			listaAlumnos[menor],listaAlumnos[x]=listaAlumnos[x],listaAlumnos[menor]

def menorMatricula(a1, a2):
	return a1[0]<a2[0]

def menorAltura(a1, a2):
	return a1[1]<a2[1]

def rango(listaAlumnos):
	alumnoMayor=listaAlumnos[0]
	alturaMayor=alumnoMayor[1]
	for t in listaAlumnos:
		altura=t[1]
		if altura>alturaMayor:
			alumnoMayor=t
			alturaMayor=alumnoMayor[1]
	alumnoMenor=listaAlumnos[0]
	alturaMenor=alumnoMenor[1]
	
	for t in listaAlumnos:
		altura=t[1]
		if altura<alturaMenor:
			alumnoMenor=t
			alturaMenor=alumnoMenor[1]
	return (alumnoMenor,alumnoMayor)

def mediaDesvEst(listaAlumnos):
	nAlumnos=len(listaAlumnos)
	desv=0
	media=0
	for t in listaAlumnos:
		media+=t[1]
	media/=nAlumnos
	for t in listaAlumnos:
		desv+=(t[1]-media)**2
	desv=math.sqrt(desv/nAlumnos)
	return (media,desv)

def altos(listaAlumnos,media,desv):
	nAltos=0
	suma=media+desv
	for matricula, altura in listaAlumnos:
		if altura>suma:
			nAltos+=1
	return nAltos

def secuencial(matricula,listaAlumnos):
	for t in listaAlumnos:
		if matricula==t[0]:
			return t[1]
	else:
		return None




listaAlumnos=leeDatos()
print("\nLista de alumnos desordenada:\n")
despliegaDatos(listaAlumnos)

print("\nLista de alumnos ordenada por matrículas:\n")
ordSeleccion(listaAlumnos,menorMatricula)
despliegaDatos(listaAlumnos)

print("\nLista de alumnos ordenada por alturas:\n")
ordSeleccion(listaAlumnos,menorAltura)
despliegaDatos(listaAlumnos)

menorMayor=rango(listaAlumnos)
print("\nLa altura menor le pertenece al alumno con matrícula "+str(menorMayor[0][0])+" y es de "+str(menorMayor[0][1])+" metros.")
print("\nLa altura mayor le pertenece al alumno con matrícula "+str(menorMayor[1][0])+" y es de "+str(menorMayor[1][1])+" metros.")


mediaDesvEst=mediaDesvEst(listaAlumnos)
print("\nMedia de alturas: "+str(mediaDesvEst[0]))
print("Desviación estándar de alturas: "+str(mediaDesvEst[1]))

alturaMayor=altos(listaAlumnos,mediaDesvEst[0],mediaDesvEst[1])
print("\nLa cantidad de alumnos con altura mayor a la media es de: "+str(alturaMayor))

print("\n----------------------------------------------------------")
print("\nConsultar altura de un alumno en base a la matrícula.")

while(True):
	matricula=int(input("\nIntroduzca la matricula del alumno a consultar(0 para terminar): "))
	if matricula==0:
		break
	altura=secuencial(matricula,listaAlumnos)
	if altura!=None:
		print("El alumno con matricula "+str(matricula)+" tiene una altura de "+str(altura)+" metros.")
	else:
		print("No se encontró un alumno con matricula "+str(matricula)+". Intente nuevamente.")
