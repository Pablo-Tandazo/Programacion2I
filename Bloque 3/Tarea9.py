#1.	Crear una función multiplicar(x, y) que retorne el producto de dos números.
def multiplicar (x , y):
    producto=x*y
    return producto


print("La multiplicacion es: ",multiplicar(4,8))

# ----------------------------------------------------------------------------

#2.	Crear una función es_par(numero) que retorne True si el número es par.

def es_par(num):
    return num % 2 == 0


print(es_par(8))

#----------------------------------------------------------------------------
#3.	Crear una función presentarse(nombre, edad) que imprima un mensaje con tus datos.
def presentarse(nombre, edad):
    print(f"Hola mi nombre es {nombre}, tengo {edad} años")

presentarse("Pablo", 28)