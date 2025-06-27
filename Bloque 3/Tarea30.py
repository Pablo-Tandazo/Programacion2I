#contador de palabras en un archivo 
with open("mi_documento.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    palabras = contenido.split()
    print(f"El archivo contiene {len(palabras)} palabras.")
