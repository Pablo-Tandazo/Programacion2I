# RECCORIENDO UN STRING 
#1  cuenta cuantas letras hay en una palabra 
print("EJERCICIO 1")

pala= "Andres"
con=0
for palabra in pala:
    palabra=len(pala)
print("La palabra contiene =" , palabra ,"letras")

#2 Imprime cada letra de una palabra en una linea distinta.
print("EJERCICIO 2")
Palabra="Pablo"

for Conteo in Palabra:
    print(Conteo)

#3 Reemplaza las vocales por un arterisco
print("EJERCICIO 3")

palabra = "Pablo"
nueva_palabra = ""

for letra in palabra:
    if letra.lower() in "aeiou":
        nueva_palabra += "*"
    else:
        nueva_palabra += letra

print(nueva_palabra)

#4 Cuenta cuantas veces aparece la letra "e"
print("EJERCICIO 4")
Letras=["elefante"]
for con in Letras:
    contar = con.count('e')
    print(contar)
#5 Invierte un string manuelamente (sin slicing)

Palabra="hola"

invertir=""

for letra in Palabra:
    invertir=letra+invertir
print("la palabra invertida es= ", invertir)


#6 Imprime solo las consonates de una palabra.
palabra = "hola"
for letra in palabra:
    if letra not in "aeiou":
        print(letra)

#7 Determina si una palabra tiene letras repetidas
palabra = "hoola"
repetida = False

for letra in palabra:
    if palabra.count(letra) > 1:
        repetida = True
        

if repetida:
    print("Tiene letras repetidas")
else:
    print("No tiene letras repetidas")

#8 Muestra cada caracter con su posicion.
palabra = "hola"
for i in range(len(palabra)):
    print(f"Posición {i}: {palabra[i]}")

#9  Verifica si hay algun numero en la cadena.

cadena = "h0la"
hay_numero = False

for caracter in cadena:
    if caracter.isdigit():
        hay_numero = True
    

if hay_numero:
    print("Hay al menos un número")
else:
    print("No hay números")

#10 covierte cada letra a su codigo ANCII

palabra = "hola"
for letra in palabra:
    print(f"{letra}: {ord(letra)}")