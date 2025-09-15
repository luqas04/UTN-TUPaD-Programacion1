import random

# Crear una matriz 5x5 con ceros
carton = []

for i in range(5):            # filas
    fila = []
    for j in range(5):        # columnas
        fila.append(0)        # valor inicial
    carton.append(fila)

# Generar 25 números únicos entre 1 y 50
numeros = random.sample(range(1, 51), 25)

def mostrar_carton(carton):
    for fila in carton:
        print(" ".join(f"{n:2}" for n in fila))  # alineado
    print()

# Transformarlos en matriz 5x5
carton = []
for i in range(5):
    fila = numeros[i*5:(i+1)*5]
    carton.append(fila)

# Mostrar el cartón
mostrar_carton(carton)

numeros_sorteados = list(range(1, 51))
random.shuffle(numeros_sorteados)

for numero in numeros_sorteados:
    input("Presiona Enter para continuar...")
    print(f"Sorteo: {numero}")

    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True

    if encontrado:
        print(f"El número {numero} está en el cartón (reemplazado por 0).")
    else:
        print(f"El número {numero} no aparece en el cartón.")

    mostrar_carton(carton)

    # Comprobar si hay bingo (todas las filas son ceros)
    if all(all(num == 0 for num in fila) for fila in carton):
        print("¡Bingo!")
        
   
    

