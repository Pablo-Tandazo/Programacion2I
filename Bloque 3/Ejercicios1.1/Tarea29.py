# 1 Imprime todos los elementos de una lista de frutas 
print("EJERCICIO 1")
frutas=["Manzana", "banana", "limon", "pera", "durazno", "Mango", "Sandia"]

for i in frutas:
    print(i)

#2 Calcula la suma de una lista de numeros.
print("EJERCICIO 2")
numero = [1, 2, 10, 15, 7, 8]

suma= 0
for i in numero:
    suma += i
    print(suma)

#3 Muestra los nombres de los estudiantes en un curso 
print("EJERCICIO 3")
Alumnos=["Sammy", "Mateo", "Yadira", "Jeremy", "Justin", "Julio", "Andy", "Richard", "Mauro", "Cristian", "Roman", "Edwin", "Josue"]

for x in Alumnos:
    print(x)

#4 Indica cuantas palabras hay con mas de 5 letras 
print("EJERCICIO 4")
Palabras=["Sammy", "Mateo", "Yadira", "Jeremy", "Justin", "Julio", "Andy", "Richard", "Mauro", "Cristian", "Roman", "Edwin", "Josue"]
contador = 0

for palabra in Palabras:
    if len(palabra)>5:
        contador +=1
print("Las palabras con mas de 5 letras son = ", contador)
  
#5 Imprime el doble de cada numero de la lista
print("EJECICIO 5")

num = [1, 2, 10, 15, 7, 8]

for nume in num:
    nume = nume*2
    print("El doble es= ",nume)

#6 Muestra solo los elementos que contiene la letra "a"
print("EJERCICIO 6")
Letras=["Kiwi", "banana", "limon", "pera", "durazno", "Mango", "Sandia"]

for a in Letras:
    if "a" in a:
        print("las palabras que contiene la letra a son = " , a)

#7 Determina cuantos numeros son mayores que 50;

N=[100,2,500,10,7,9,82]

for w in N:
    if w > 50:
        print("Los numeros mayores a 50 son= " , w)

#8 Crea una lista con los cuadrados de los elementos originales 
print("EJERCICIO 8")

#9 Filtra y muestra solo los elementos que sean strings
print("EJERCICIO 9")
L=["Pablo ",20,"frutas", 10 , 3, "palabra"]

for m in L:
    if type(m) == str:
         print(m)

#10 cambia todos los nombres a mayúsculas.
Nombres=["Sammy", "Mateo", "Yadira", "Jeremy", "Justin", "Julio", "Andy", "Richard", "Mauro", "Cristian", "Roman", "Edwin", "Josue"]
Nombres_may= []
for nombre in Nombres:
    Nombres_may.append(nombre.upper())
    print(Nombres_may)