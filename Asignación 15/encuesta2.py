#Programa para determinar cuantos alumnos hay en cada categoría, de cada sexo y de cada carrera.
#Jesús Eduardo Ramírez Cota 00000165732
print("Programa para determinar cuantos alumnos hay en cada categoría, de cada sexo y de cada carrera.")

def leeEncuesta():
	nAlumno=1
	alumnos=[]
	while(True):
		matricula=int(input("\nIntroduzca la matrícula del alumno "+str(nAlumno)+" (0 para terminar)."))
		if(matricula==0):
			break
		sexo=input("Introduzca el sexo del alumno (M/F): ").upper()
		carrera=input("Introduzca la carrera del alumno (siglas ISW/IE/IC etc.): ").upper()
		alumno=(matricula,sexo,carrera)
		alumnos.append(alumno)
		nAlumno+=1
	return alumnos

def despEncuesta(alumnos):
	print("\n-----Datos----")
	print("| Matrícula | Sexo | Carrera |")
	for alumno in alumnos:
		print("|   "+str(alumno[0])+"   |  "+str(alumno[1])+"  |   "+str(alumno[2])+"  |\n")

def clasificaAlumnosCategoria(alumnos):
	alumnosCategoria=dict()
	for matricula,sexo,carrera in alumnos:
		t=(sexo,carrera)
		if t not in alumnosCategoria:
			alumnosCategoria[t]=1
		else:
			alumnosCategoria[t]=alumnosCategoria[t]+1
	return alumnosCategoria

def despAlumnosCategoria(alumnosCategoria):
	print("\n----Alumnos por Categoria----")
	print("| Sexo | Carrera | Alumnos |")
	for k, valor in alumnosCategoria.items():
		print("|   "+str(k[0])+"   |  "+str(k[1])+"  |   "+str(valor)+"  |\n")

def clasificaAlumnosSexo(alumnosCategoria):
	alumnosSexo=dict()
	for k in alumnosCategoria:
		valor=alumnosCategoria.get(k)
		sexo=k[0]
		if sexo not in alumnosSexo:
			alumnosSexo[sexo]=valor
		else:
			alumnosSexo[sexo]=alumnosSexo[sexo]+valor
	return alumnosSexo

def despAlumnosSexo(alumnosSexo):
	print("\n-Alumnos según su sexo-")
	print("------------------")
	print("| Sexo | Alumnos |")
	for k, valor in alumnosSexo.items():
		print("|   "+str(k)+"   |  "+str(valor)+"  |\n")

def clasificaAlumnosCarrera(alumnosCategoria):
	alumnosCarrera=dict()
	for k in alumnosCategoria:
		valor=alumnosCategoria.get(k)
		carrera=k[1]
		if carrera not in alumnosCarrera:
			alumnosCarrera[carrera]=valor
		else:
			alumnosCarrera[carrera]=alumnosCarrera[carrera]+valor
	return alumnosCarrera

def despAlumnosCarrera(alumnosCarrera):
	print("\n--Alumnos por carrera--")
	print("-----------------------")
	print("| Carrera | Alumnos |")
	for k, valor in alumnosCarrera.items():
		print("|   "+str(k)+"   |  "+str(valor)+"  |\n")



alumnos=leeEncuesta()

despEncuesta(alumnos)

alumnosCategoria=clasificaAlumnosCategoria(alumnos)

despAlumnosCategoria(alumnosCategoria)

alumnosSexo=clasificaAlumnosSexo(alumnosCategoria)

despAlumnosSexo(alumnosSexo)

alumnosCarrera=clasificaAlumnosCarrera(alumnosCategoria)

despAlumnosCarrera(alumnosCarrera)