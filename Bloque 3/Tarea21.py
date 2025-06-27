#1 CONTEO REGRASIVO 
n=10
while n > 0:
    print(n)
    n -=1
print("DESPEGUE")

#2 Adivina la palabre secreta
palabra_secreta = "python"

while True:
    intento = input("Adivina la palabra secreta: ")
    if intento == palabra_secreta:
        print("¡Has adivinado la palabra!")
        break
    else:
        print("Inténtalo de nuevo.")
#3 Procesador de entradas con continue
while True:
    Entrada= input("Ingresa cualquier palabra:   ")
    if Entrada == "#":
        continue
    elif Entrada=="listo":
        print("Procesamineto Terminado")
        break
    else:
        print(Entrada.upper())

#4 Lista de invitados con for 
Lista=["Ana","Luis","carla","Pedro"]

for nombre in Lista:
    print(f"Hola {nombre}!Bienvenida a la fiesta!")
#5 Encontrando el numero mayor 
numeros = [3, 41, 12, 9, 74, 15, 1, 55]
mayor_hasta_ahora = numeros[0]

for numero in numeros:
    if numero > mayor_hasta_ahora:
        mayor_hasta_ahora = numero

print("El número más grande es:", mayor_hasta_ahora)

#6 Conteo de elementos pares
numeros=[2,5,8,11,14,17,20,23]
contador=0
for numero in numeros:
    if numero % 2 == 0:
        contador  += 1
print("El numero de pares es: ",contador)

#7 Suma de todos los numero

numero=[10,20,30,40,50]
suma_total=0
for suma in numero:
    suma_total += suma
print("La suma total es:  ", suma_total)

#8 Calculo de promedio.
lista=[10,15,20,25,30]
contador = 0
suma = 0
for promedio in lista:
    contador += 1
    suma += promedio

promedio = suma/contador
print("El promedio es: ", promedio)

#9 Filtrando numeros mayores que un valor 

numeros = [5, 25, 12, 33, 18, 45, 7]
numero_umbral=int(input("Ingresa cualquier numero: "))

for numero in numeros:
    if numero > numero_umbral:
        print( numero)

#10 Busqueda de un valor especifico.
numeros = [9, 41, 12, 3, 74, 15]
numero_encntrado = False

for valor  in numeros:
    if valor == 3:
        numero_encntrado = True
        break
print("El valor 3 fue encontrado " , numero_encntrado)

#11 Encontrando el numero menor 
numeros = [30, 10, 5, 25, 50, 2]
menor_hasta_ahora = None

for numero in numeros:
    if menor_hasta_ahora is None or numero < menor_hasta_ahora:
        menor_hasta_ahora = numero

print("El número más pequeño es:", menor_hasta_ahora)







