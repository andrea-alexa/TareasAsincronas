integrante1_nombre = "Antony Eleazar "
integrante1_apellido = "Tobías Beltrán"
integrante1_sexo = "masculino"
integrante1_edad = 17

integrante2_nombre = "Andrea Alexandra "
integrante2_apellido = "Nuñez Morán"
integrante2_sexo = "femenino"
integrante2_edad = 17

integrante3_nombre = "Kevin Francisco "
integrante3_apellido = "Menjivar Calderón "
integrante3_sexo = "masculino"
integrante3_edad = 17

integrante4_nombre = "Franklin Geovany "
integrante4_apellido = "Gómez Valle"
integrante4_sexo = "masculino"
integrante4_edad = 17

integrante5_nombre = "Mauricio Imanol "
integrante5_apellido = "García Romero"
integrante5_sexo = "masculino"
integrante5_edad = 17


concatenacion1 = integrante1_nombre + integrante1_apellido

concatenacion2 = integrante2_nombre + integrante2_apellido

concatenacion3 = integrante3_nombre + integrante3_apellido

concatenacion4 = integrante4_nombre + integrante4_apellido

concatenacion5 = integrante5_nombre + integrante5_apellido


print("El integrante 1 del grupo es", concatenacion1) 
print("El integrante 2 del grupo es", concatenacion2)
print("El integrante 3 del grupo es", concatenacion3) 
print("El integrante 4 del grupo es", concatenacion4) 
print("El integrante 5 del grupo es", concatenacion5)

print("----------------------------------------------------------------------------------------")
cadena = concatenacion1
subcadena = cadena[:6]
subcadena2 = cadena [7:15]
subcadena3 = cadena [15:21]
subcadena4 = cadena [22:30]

print("---Subcadenas de integrante 1---")
print("subcadena1:",subcadena)
print("subcadena2:",subcadena2)
print("subcadena3:",subcadena3)
print("subcadena4:",subcadena4)


print("----------------------------------------------------------------------------------------")
print("Sexo y edades de los integrantes:")

print("Sexo de",integrante1_nombre,"es",integrante1_sexo,"y su edad es", integrante1_edad, "años" )
print("Sexo de",integrante2_nombre,"es",integrante2_sexo,"y su edad es", integrante2_edad, "años" )
print("Sexo de",integrante3_nombre,"es",integrante3_sexo,"y su edad es", integrante3_edad, "años" )
print("Sexo de",integrante4_nombre,"es",integrante4_sexo,"y su edad es", integrante4_edad, "años" )
print("Sexo de",integrante5_nombre,"es",integrante5_sexo,"y su edad es", integrante5_edad, "años" )

print("----------------------------------------------------------------------------------------")

edades = (17 + 17 + 17 + 17 + 17)
promedio_de_edades = (17 + 17 + 17 + 17 + 17) /5
print("El promedio de las edades es:", promedio_de_edades)

print("----------------------------------------------------------------------------------------")

edad_salida_carrera = 17 + 5
print("El integrante 1: ", concatenacion1,"tendrá", edad_salida_carrera, "años al salir de la carrera.")
edad_salida_carrera = 17 + 5
print("El integrante 2: ", concatenacion2, "tendrá",edad_salida_carrera, "años al salir de la carrera.")
edad_salida_carrera = 17 + 5
print("El integrante 3: ", concatenacion3, "tendrá", edad_salida_carrera, "años al salir de la carrera.")
edad_salida_carrera = 17 + 5
print("El integrante 4: ", concatenacion4, "tendrá", edad_salida_carrera, "años al salir de la carrera.")
edad_salida_carrera = 17 + 5
print("El integrante 5: ",concatenacion5, "tendrá", edad_salida_carrera, "años al salir de la carrera.")