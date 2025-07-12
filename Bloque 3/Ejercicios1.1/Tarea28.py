# Tabla de multiplicar segun el usuario 

x=int(input("Ingresa el numero: "))
for i in range (1, 11):
    Mul=i*x
    print("La multiplicacion es= ", Mul)


# % da el residuo de un producto
# != signifoca que no es igual 

for i in range(15 , 31):
    if i % 2 != 0 :
        print(i)