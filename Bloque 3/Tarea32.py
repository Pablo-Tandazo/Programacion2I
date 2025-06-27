import os

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("    MENÚ DE GESTIÓN DE ARCHIVOS")
    print("="*40)
    print("1. Crear archivo")
    print("2. Nuevo archivo")
    print("3. Escribir en un archivo")
    print("4. Eliminar archivo")
    print("5. Salir")
    print("="*40)

def crear_archivo():
    """Crea un nuevo archivo vacío"""
    nombre = input("Ingresa el nombre del archivo (con extensión): ")
    try:
        with open(nombre, 'w') as archivo:
            pass  # Crea archivo vacío
        print(f"✅ Archivo '{nombre}' creado exitosamente.")
    except Exception as e:
        print(f"❌ Error al crear el archivo: {e}")

def nuevo_archivo():
    """Crea un nuevo archivo con contenido inicial"""
    nombre = input("Ingresa el nombre del archivo (con extensión): ")
    contenido = input("Ingresa el contenido inicial del archivo: ")
    try:
        with open(nombre, 'w') as archivo:
            archivo.write(contenido)
        print(f"✅ Archivo '{nombre}' creado con contenido inicial.")
    except Exception as e:
        print(f"❌ Error al crear el archivo: {e}")

def escribir_archivo():
    """Escribe contenido en un archivo existente"""
    nombre = input("Ingresa el nombre del archivo: ")
    
    if not os.path.exists(nombre):
        print(f"❌ El archivo '{nombre}' no existe.")
        crear = input("¿Deseas crearlo? (s/n): ").lower()
        if crear != 's':
            return
    
    print("\nModos de escritura:")
    print("1. Sobrescribir archivo completo")
    print("2. Agregar al final del archivo")
    
    try:
        modo = input("Selecciona el modo (1 o 2): ")
        contenido = input("Ingresa el contenido a escribir: ")
        
        if modo == "1":
            with open(nombre, 'w') as archivo:
                archivo.write(contenido)
            print(f"✅ Contenido sobrescrito en '{nombre}'.")
        elif modo == "2":
            with open(nombre, 'a') as archivo:
                archivo.write("\n" + contenido)
            print(f"✅ Contenido agregado a '{nombre}'.")
        else:
            print("❌ Modo no válido.")
    except Exception as e:
        print(f"❌ Error al escribir en el archivo: {e}")

def eliminar_archivo():
    """Elimina un archivo existente"""
    nombre = input("Ingresa el nombre del archivo a eliminar: ")
    
    if not os.path.exists(nombre):
        print(f"❌ El archivo '{nombre}' no existe.")
        return
    
    # Mostrar contenido antes de eliminar
    try:
        with open(nombre, 'r') as archivo:
            contenido = archivo.read()
        print(f"\nContenido actual de '{nombre}':")
        print("-" * 30)
        print(contenido[:200] + "..." if len(contenido) > 200 else contenido)
        print("-" * 30)
    except:
        print("No se pudo mostrar el contenido del archivo.")
    
    confirmar = input(f"¿Estás seguro de eliminar '{nombre}'? (s/n): ").lower()
    
    if confirmar == 's':
        try:
            os.remove(nombre)
            print(f"✅ Archivo '{nombre}' eliminado exitosamente.")
        except Exception as e:
            print(f"❌ Error al eliminar el archivo: {e}")
    else:
        print("❌ Eliminación cancelada.")

def main():
    """Función principal del programa"""
    print("¡Bienvenido al Gestor de Archivos!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una opción (1-5): ")
            
            if opcion == "1":
                crear_archivo()
            elif opcion == "2":
                nuevo_archivo()
            elif opcion == "3":
                escribir_archivo()
            elif opcion == "4":
                eliminar_archivo()
            elif opcion == "5":
                print("¡Gracias por usar el Gestor de Archivos! 👋")
                break
            else:
                print("❌ Opción no válida. Por favor selecciona una opción del 1 al 5.")
                
        except KeyboardInterrupt:
            print("\n\n❌ Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()