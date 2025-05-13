#Sumar números ingresados por el usuario hasta que ingrese 0.
print("1. Sumar números ingresados por el usuario hasta que ingrese 0. :")
numero=1
suma =0
while numero !=0:
    numero=int(input("Ingrese un numero= "))
    suma += numero

print(f"La suma total de los numeros ingresados es= {suma}")
       
#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
print("3. Adivinar un número aleatorio entre 1 y 100")
import random # Importamos la libreria random para que me genere un numero aleatorio 
numeroSecreto = random.randint(1,100) # hace que genere un numero alatorio enter dicho rango 
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
print("3. Validar contraseña:")
contraseña = "2656"
usuario = ""
while usuario != contraseña:
    usuario = input("Ingresa la contraseña: ")
print("Contraseña válida: acceso permitido")

#Simular un cajero automático (menú: retirar, depositar, salir).
print("4. Cajero automático:")
saldo = 1000
opcion = ""
while opcion != "3":
    print("1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        monto = float(input("cuanto vas a retirar: "))
        if monto <= saldo:
            saldo -= monto
            print(f"Saldo disponible: {saldo}")
        else:
            print("Fondos insuficientes. intenta nuevamente")
    elif opcion == "2":
        monto = float(input("Dinero a depositar: "))
        saldo += monto
        print(f"Tu saldo es: {saldo}")

    elif opcion == "3":
        print("Gracias por usar este cajero. Regresa pronto")

    else:
        print("ups Opcion Valida. quieres volver a intentar")

#Calcular la raíz cuadrada por aproximación (método babilónico).
print("5. Calcular la raiz cuadrada por aproximacion")
numero = float(input("Número: "))
x = numero
y = 1
e = 0.000001
while abs(x - y) > e:
    x = (x + y) / 2
    y = numero / x
print(f"La raíz aproximada es: {x}")

#Contar dígitos de un número entero (ej: 456 → 3).
print("6. Contar digitos de un numero entero")

numero = int(input("Número de forma entera: "))
contador = 0
n = abs(numero)
while n > 0:
    n //= 10
    contador += 1
print(f"el numero tiene: {contador} digitos")
#Generar la secuencia de Fibonacci hasta un límite.
print("7. Fibonacci hasta un límite:")
limite = int(input("Ingresa un Límite: "))
a, b = 0, 1
while a <= limite:
    print(a," ")
    a, b = b, a + b
print()
#Encontrar números primos en un rango dado.
print("8. Números primos en un rango:")
inicio = int(input("Ingresa un valor de inicio: "))
fin = int(input("ingresa un valor Final: "))
n = inicio
while n <= fin:
    es_primo = True
    if n < 2:
        es_primo = False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                es_primo = False
                break
            i += 1
    if es_primo:
        print(n, end=" ")
    n += 1
print()
#Simular un temporizador (contar regresivamente desde N).
import time
print("9. Temporizador regresivo:")
n = int(input("Desde qué número?: "))
while n >= 0:
    print(n)
    time.sleep(1)
    n -= 1
print("¡Se acabo el tiempo!")
#Leer archivos línea por línea hasta fin de archivo.
print("10. Leer archivo línea por línea:")
archivo_nombre = input("Nombre del archivo: ")
try:
    with open(archivo_nombre, "r") as archivo:
        linea = archivo.readline()
        while linea:
            print(linea.strip())
            linea = archivo.readline()
except FileNotFoundError:
    print("Archivo no encontrado.")

# Visualizar los 5 primeros numeri con mientras = WHILE

contador = 0
while contador <= 10:
    print("numeros: " , contador)
    contador += 1
