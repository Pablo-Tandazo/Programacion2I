# CREAR MENU 

import os
def menu():
    while True:
        print("MENU PRINCIPAL DE ARCHIVOS")
        print("1. CREAR ARCHIVO")
        print("2. NUEVO")
        print("3. ESCRIBIR")
        print("4. ELIMINAR")
        print("5. SALIR")

        Opcion=input("Elige cualquier opcion del 1-5:   ")

        if Opcion == "1":
            crear_archivo()
        elif Opcion == "2":
            nuevo_archivo()
        elif Opcion == "3":
            escribir_en_archivo()
        elif Opcion == "4":
            eliminar_archivo()
        elif Opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
1
1menu()
