#Escritra en un archivo de texto 
with open("output.txt", "a", encoding="utf-8") as archivo:
    while True:
        texto = input("Escribe una línea de texto (o 'salir' para terminar): ")
        if texto.lower() == "salir":
            break
        archivo.write(texto + "\n")
