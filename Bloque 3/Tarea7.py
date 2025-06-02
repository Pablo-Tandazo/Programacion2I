#Crear una funcion que imprima un mensaje 
def saludo():
    print("HOLA MUNDO")
saludo()
#Funcion con  una argumento
def saludar(nombre):
    print(f"Hola,{nombre}")
saludar("Pablo")
#suma de dos numeros
def suma(a , b):
    return a + b
print(suma(5, 3))
#Calcular el salario 
def salario(horas, tarifa):
    if horas > 40:
        hextras=horas-40
        pago=(40*tarifa)+(hextras*tarifa*1.5)
    else:
        pago=horas * tarifa
    return pago

print(salario(45,10))
#Funcion para determinar el mayor caracter
def M_Caracter(cadena):
    return max(cadena)
print(M_Caracter("programacion"))
#conversion de tipo 
def C_flotante(valor):
    try:
        return float(valor)
    except ValueError:
        return"error:Imposible transformar a flotante"
print(C_flotante("abc"))
#Funcion que retorna un saludo en diferentes idiomas 
def S_idioma(lang):
    if lang == "es":
        return "HOLA"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "hello"
print(S_idioma("fr"))
#Comprobar si un numero es par 
def numero_par(num):
    return num %2==0
print(numero_par(5))
#Concatenar cadenas 
def Concatenar(cadena1,cedena2):
    return cadena1+cedena2

print(Concatenar("pablo" , " Andres"))
#Calcular promedio
def pro(lista):
    if not lista:
        return 0
    return sum(lista)/len(lista)
print(pro([4,5,6]))
#Contar vocales
def contar_v(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for c in cadena if c in vocales)
print(contar_v("Hola mundo"))
#Revertir cadena
def invertir(cadena):
    return cadena[::-1]
print(invertir("Pablo"))
#Tabla de multiplicar 
def tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
tabla(5)
#Funcion sin parametros 
def mensaje():
    print("mi nombre es pablo.")
    print("Tengo 28 años.")
    print("Y soy una aguila roja.")
mensaje()
#Funcion que retorne el numero mas pequeño 
def menor_valor(lista):
    if not lista:
        return None
    return min(lista)
print(menor_valor([3,-2,5,-9]))
#Calcular factorial 
def factorial(n):
    if n < 0:
        return "Error: factorial no definido para negativos"
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
print(factorial(5))
#Determinar si un numero es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
print(es_primo(7))
#Repetir una cadena n veces
def repetir(cadena, n):
    return cadena * n
print(repetir("Pablo  " , 3 ))
#Funcion con multiples parametros 
def descripcion(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
descripcion("Pablo " , 28 , "Azogues")
#Verificar palindromo 
def palindromo(cadena):
    cadenaL= "".join(c for c in cadena if c.isalnum()).lower()
    return cadenaL==cadenaL[::-1]
print(palindromo("Anita lava la tina"))      
print(palindromo("reconocer"))               
print(palindromo("Python"))                 
print(palindromo("¿Acaso hubo búhos acá?"))