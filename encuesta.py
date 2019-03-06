# Jesús Eduardo Ramírez Cota - 165732
# Programa que calcula distintos porcentajes de acuerdo a datos encuestados.
nAlumnos = 0
totalAlumnos = 0
totalEdadesHombres = 0
totalEdadesMujeres = 0
hombresForaneos = 0
mujeresForaneas = 0
hombresSolos = 0
mujeresCompartir = 0
mujeres = 0
hombres = 0
alumnosCasaAsistencia = 0
while True :
    viviendaDeseada = ""
    edad = int(input("Edad en años: "))
    if edad == 0: break
    nAlumnos+=1
    sexo = input("Sexo (M) ó (F): ")
    procedencia = input("Procedencia (L)Local ó (F)Fóraneo :")
    if procedencia == "F": 
        viviendaDeseada = input("Vivienda deseada (A)Casa de asistencia, (C)Compartir casa, (S)Vivir solo :")
        if viviendaDeseada== "A" : alumnosCasaAsistencia+=1
    if sexo == "M" : 
        hombres+=1
        totalEdadesHombres +=edad
        if procedencia == "F" : 
            hombresForaneos+=1
            if viviendaDeseada == "S": hombresSolos+=1
    else :
        mujeres+=1
        totalEdadesMujeres+=edad
        if procedencia == "F" :
            mujeresForaneas+=1
            if viviendaDeseada == "C": mujeresCompartir+=1
if nAlumnos > 0 :
    print("Número de alumnos encuestados: "+str(nAlumnos))
    print("Edad promedio de alumnos:")
    if hombres > 0 :
        print("- Hombres = " +str(totalEdadesHombres/hombres)+" años")
    if mujeres > 0:
        print("- Mujeres = "+str(totalEdadesMujeres/mujeres)+" años")
    print("Porcentaje de alumnos foráneos: Hombres = "+str(round(hombresForaneos*100/nAlumnos, 2))+"%, Mujeres = "+str(round(mujeresForaneas*100/nAlumnos, 2))+"%")
    print("Porcentaje de alumnos que desena vivr en casa de asistencia: "+str(round(alumnosCasaAsistencia*100/nAlumnos, 2))+"%")
    print("Porcentaje de alumnos mujeres que desean compartir casa : "+str(round(mujeresCompartir*100/nAlumnos,2)))
    print("Porcentaje de alumnos hombres que desean vivir solos: "+str(round(hombresSolos*100/nAlumnos, 2)))
