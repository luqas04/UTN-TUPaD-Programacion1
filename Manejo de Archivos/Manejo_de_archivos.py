import textwrap

# Lectura de archivo y muestra de productos
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # Quitamos espacios y saltos de línea
        linea = linea.strip()
        # Separamos por coma
        datos = linea.split(",")
        
        # Asignamos variables y convertimos precio y cantidad
        nombre = datos[0]
        precio = float(datos[1])
        cantidad = int(datos[2])
        
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


# Función para agregar un nuevo producto al archivo
def agregar_producto(nombre, precio, cantidad):
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"\n{nombre},{precio},{cantidad}")

 
# Solicitamos al usuario un nuevo producto
nuevo_producto = input("Ingrese el nuevo producto (nombre,precio,cantidad): ")

nombre, precio, cantidad = nuevo_producto.split(",")
agregar_producto(nombre, float(precio), int(cantidad))


productos = []
# Leemos todos los productos y los almacenamos en una lista de diccionarios
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # Quitamos espacios y saltos de línea
        linea = linea.strip()
        # Separamos por coma
        datos = linea.split(",")
        # Creamos un diccionario para cada producto
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        
        productos.append(producto)
# Mostramos todos los productos almacenados
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

producto_buscar = input("Ingrese el nombre del producto a buscar: ")
# Buscamos el producto en la lista
for p in productos:
    # Comparamos ignorando mayúsculas/minúsculas
    if p['nombre'].lower() == producto_buscar.lower():
        # Si encontramos el producto, mostramos sus detalles
        print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        break
else:
    print("Producto no encontrado.")

# Abrimos el archivo en modo escritura (sobrescribe todo)
with open("productos.txt", "w", encoding="utf-8") as archivo:
    # Escribimos todos los productos desde la lista
    for p in productos:
        # Escribimos cada producto en el formato nombre,precio,cantidad
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        # Escribimos la línea en el archivo
        archivo.write(linea)

print("Archivo productos.txt actualizado correctamente.")

