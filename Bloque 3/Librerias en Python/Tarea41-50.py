# 41 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
productos = {
    "manzanas": 0.5,
    "pan": 1.0,
    "leche": 1.2,
    "queso": 2.5
}

busqueda = input("¿Qué producto deseas buscar? ").lower()

if busqueda in productos:
    print(f"{busqueda.title()} cuesta ${productos[busqueda]:.2f}")
else:
    print("Producto no encontrado.")
