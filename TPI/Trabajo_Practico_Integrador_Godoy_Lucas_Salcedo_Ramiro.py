import csv
from funciones_opciones import menu, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas

def leer_csv(ruta):
    paises = []
    with open(ruta, newline='', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila["poblacion"] = int(fila["poblacion"])
            fila["superficie"] = int(fila["superficie"])
            paises.append(fila)
    return paises


def main():

    paises = leer_csv("paises.csv")

    while True:
        opcion = menu()
        if opcion == "1":
            buscar_pais(paises)
        elif opcion == "2":
            filtrar_paises(paises)
        elif opcion == "3":
            ordenar_paises(paises)
        elif opcion == "4":
            mostrar_estadisticas(paises)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

main()