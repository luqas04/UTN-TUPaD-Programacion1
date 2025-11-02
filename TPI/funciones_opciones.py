def menu():
    print("\n--- Gestión de Datos de Países ---")
    print("1. Buscar país")
    print("2. Filtrar países")
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("5. Salir")
    return input("Elegí una opción: ")


def buscar_pais(paises):
    if not paises:
        print("No hay datos disponibles.")
        return
    
    nombre = input("Ingresá el nombre del país a buscar: ")
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"País encontrado: {p}")
            return
    print("País no encontrado.")

def filtrar_paises(paises):
    if not paises:
        print("No hay datos disponibles.")
        return
    
    continente = input("Ingresá el continente para filtrar: ")
    
    # Creamos una lista vacía para ir guardando los países que cumplen la condición
    paises_filtrados = []
    
    # Recorremos la lista de países
    for pais in paises:
        # Comparamos el continente en minúsculas para que no importe mayúsculas/minúsculas
        if pais["continente"].lower() == continente.lower():
            paises_filtrados.append(pais)
    
    # Mostramos los resultados
    if paises_filtrados:
        print(f"\n Países en {continente}:")
        print("-" * 40)
        for p in paises_filtrados:
            print(f"• {p['nombre']}")
            print(f"  Población: {p['poblacion']:,}".replace(",", "."))
            print(f"  Superficie: {p['superficie']:,} km²".replace(",", "."))
            print("-" * 40)
    else:
        print(f"No se encontraron países en el continente '{continente}'.")

def ordenar_paises(paises):
    if not paises:
        print("No hay datos disponibles.")
        return
     
    # Pide al usuario el criterio
    criterio = input("Ingresá el criterio de ordenamiento (nombre, poblacion, superficie): ").lower()
    
    # Validamos que el criterio sea correcto
    if criterio not in ["nombre", "poblacion", "superficie"]:
        print("Criterio inválido. Usando 'nombre' por defecto.")
        criterio = "nombre"
    
    # Preguntamos de que manera quiere ordenar (ascendente o descendente)
    while True:
        respuesta = input("¿Querés orden descendente? (s/n): ").strip().lower()
        # Validamos la respuesta
        if respuesta in ["s", "n"]:
            orden_desc = respuesta == "s"  # True si es 's', False si es 'n'
            break  # Salimos del bucle cuando la respuesta es válida
        else:
             print("Respuesta inválida. Por favor, escribí 's' o 'n'.")

    # Ordenamos la lista
    paises_ordenados = sorted(paises, key=lambda x: x[criterio], reverse=orden_desc)
    
    # Mostramos solo los nombres y el valor del criterio para que sea más legible
    print(f"\nPaíses ordenados por {criterio} ({'descendente' if orden_desc else 'ascendente'}):")
    
    if criterio in ["poblacion", "superficie"]:
        for p in paises_ordenados:
            print(f"{p['nombre']}: {p[criterio]}")
    else:
        for p in paises_ordenados:
            print(f"{p[criterio]}")

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos disponibles.")
        return
    
    mayor_poblacion = max(paises, key=lambda x: x["poblacion"])
    menor_poblacion = min(paises, key=lambda x: x["poblacion"])

    total_poblacion = sum(pais["poblacion"] for pais in paises)
    promedio_poblacion = total_poblacion / len(paises)

    total_superficie = sum(pais["superficie"] for pais in paises)
    promedio_superficie = total_superficie / len(paises)

    paises_por_continente = {}
    for p in paises:
        continente = p["continente"]
        paises_por_continente[continente] = paises_por_continente.get(continente, 0) + 1

    print(f"País con mayor población: {mayor_poblacion}")
    print(f"País con menor población: {menor_poblacion}")
    print(f"Población promedio: {promedio_poblacion}")
    print(f"Superficie promedio: {promedio_superficie}")
    print("Cantidad de países por continente:")
    for continente, cantidad in paises_por_continente.items():
        print(f"{continente}: {cantidad}")
