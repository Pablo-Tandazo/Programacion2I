#Sumar números ingresados por el usuario hasta que ingrese 0.
print("1. Sumar números hasta 0:")
suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))
print("La suma total es:", suma)
   


    
#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").

import random
numeroSecreto = random.randint(1,100)
intento=None

while intento != numeroSecreto:
    intento=int(input("Adivina el numero del 1 al 100: "))
    if intento < numeroSecreto:
        print("Mayor")

    elif intento > numeroSecreto:
        print("Menor")

    else:
        print("Muy bien el numero secreo es: ", numeroSecreto)

#Validar contraseña (repetir hasta que coincida con una guardada).
Contra = "Pablo"
while True:
    Ingresa = input("Ingresa la contraseña")
    if Ingresa== Contra:
        print("La contraseña es correcta: ")

    else:
        print("La contraseña es incorrecta: intenta nuevamente")
#Simular un cajero automático (menú: retirar, depositar, salir).


#Calcular la raíz cuadrada por aproximación (método babilónico).

#Contar dígitos de un número entero (ej: 456 → 3).

#Generar la secuencia de Fibonacci hasta un límite.

#Encontrar números primos en un rango dado.

#Simular un temporizador (contar regresivamente desde N).

#Leer archivos línea por línea hasta fin de archivo.


# Visualizar los 5 primeros numeri con mientras = WHILE

contador = 0
while contador <= 10:
    print("numeros: " , contador)
    contador += 1
