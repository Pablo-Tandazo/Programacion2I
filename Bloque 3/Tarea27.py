# LEER UN ARCHIVO COMPLETO 
with open("mi_documento.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)

