# con range() - iteración con contador 
# 1 imprime los numeros del 1 al 10
print("EJERCICIO 1")
for i in range(1, 11):
    print("Numeros del 1 al 10 = ", i)

#2 imprime los numeros pares del 2 al 20
print("EJERCICIO 2")

for x in range (2, 21, 2):
    print("Numeros pares del 2 al 20  = ", x)

#3 Imprime los multiplos de 3 del 0 al 30 
print("EJERCICIO 3")

for y in range (0, 31, 3):
    print("Numeros multiplos de 3 = " , y)


# 4 cuenta hacia atras desde 10 al 1
print("EJERCICIO 4")

for numero in range(10 , 0 , -1):
    print("Numero del 10 al 1" , numero)

#5 muestra la tabla de multiplicar del 7
print("EJERCICIO 5")

tab=0
for tab in range(1 , 11):
    respuesta = tab * 7
    print("Tabla de multiplicar 7 = ", respuesta )

#6 suma todos los números del 1 al 100
print("EJERCICIO 6")

suma = 0
for z in range (0, 101):
    suma +=z
    print("Suma los numeros de 1 al 100 = ", suma)

#7 Calcula el factorial de un nmero dado 
print("EJERCICIO 7")

num = int(input("Ingresa tu numero = "))
fac = 1

for i in range(1, num +1):
    fac *= i
    print("El factorial del numero" , num, "es" , fac)



#8 Imprime los numeros impares entre 15 y  30
print("EJERCICIO 8")

for i in range(15, 30, 2):
    print("Los numeros impares son = ", i)

#9 Muestra todos los años desde 1990 hasta 2025
print("EJERCICIO 9")

for a in range(1990 , 2026):
    print("Los años son = ", a)

#10 Imprime un cuadrado de arteriscos de 5*5
print("EJERCICIO 10")
 
for z in range(1,6):
    print("*" * 5)