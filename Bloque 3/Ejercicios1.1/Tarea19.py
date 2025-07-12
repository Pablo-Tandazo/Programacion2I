# INGRESA TRES NOTAS DEL ESTUDIANTE Y CALCULA EL PROMEDIO 
#LUEGO IDENTIFICA SI PASA O NO EL AÑO CON LA SIGUINTE ESCALA 
# MENOR A 59 REPRUEBA
# ENTRE 60 Y 79 REGULAR 
#ENTRE 80 Y 89 BUENA
# ENTRE A 90 Y 100 EXCELENTE 

nota1= float(input("Ingresa tu primera nota = "))
nota2= float(input("Ingresa tu segunda nota = "))
nota3= float(input("Ingresa tu tercera nota = "))


promedio=((nota1+nota2+nota3)/3)

print(f"El promedio del estudiante es = {promedio}")


if promedio <=59:
    print("El estudiante reprueba")

elif 60<=promedio<80:
    print("El estudiante es regular ")
elif 80<=promedio<90:
    print("Es bueno el estudiante  ")
elif 90<= promedio <101:
    print("Es un exelnete estudiante")
else:
    print("El promedio no es valido")