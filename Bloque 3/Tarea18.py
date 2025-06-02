Numero_Mayor=-1
print("Antes", Numero_Mayor)
for numero in [9, 41, 12, 3, 74, 15]:
    if numero > Numero_Mayor:
        Numero_Mayor = numero
    print(Numero_Mayor, numero)
print("Despues", Numero_Mayor)