# Abrir y leer el archivo
with open("frases.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read().lower()

# Limpiar y dividir el texto
palabras = texto.replace(".", "").split()

# Contar frecuencia
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Mostrar resultados
print("Frecuencia de palabras:")
for palabra, cantidad in frecuencia.items():
    print(f"{palabra}: {cantidad}")