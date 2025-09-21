import random

# Ejercicio 1:

for i in range(0, 101):
    print(i)

# Ejercicio 2:

num = int(input("Ingresa un número entero: "))

# Asegurar que sea positivo (los dígitos no dependen del signo)
num = abs(num)

contador = 0

if num == 0:
    contador = 1
else:
    while num > 0:
        num //= 10   # División entera (quita el último dígito)
        contador += 1

print("El número tiene", contador, "dígitos.")

# Ejercicio 3: suma de números en un rango

minimo = int(input("Ingresa el rango minimo: "))

maximo = int(input("Ingresa el rango maximo: "))

for i in range(minimo, maximo + 1):
    print(f"{i + 1} + {i} = {i + (i + 1)}")

# Ejercicio 4: suma de numeros hasta que se ingresa 0

suma = 0
while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma de los números ingresados es:", suma)

# Ejercicio 5: adivinanza el numero

intentos = 0 

numero_secreto = random.randint(0, 9)

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento != numero_secreto:
        print("Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break

# Ejercicio 6: numeros pares entre 1 y 100 en forma descendente

for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)


# Ejercicio 7: suma de numeros hasta el maximo que ingresa el usuario

maximo = int(input("Ingresa el número máximo: "))
suma = 0

for i in range(1, maximo + 1):
    suma += i

print("La suma de los números desde 1 hasta", maximo, "es:", suma)

# Ejercicio 8: indicar cuántos de los números de los pedidos son pares, cuántos son impares, cuántos son negativos y cuántos son positivos

cantidad_numeros = 5
pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(cantidad_numeros):
    numero = int(input("Ingresa un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

# Ejercicio 9: promedio de 100 numeros enteros

suma = 0
cantidad = 5

for _ in range(cantidad):
    numero = int(input("Ingresa un número entero: "))
    suma += numero
    promedio = suma / cantidad

print("El promedio de los números ingresados es:", promedio)

# Ejercicio 10: inversor de digitos de un numero entero

numero = int(input("Ingresa un número entero: "))
inverso = 0
num = abs(numero)  # Trabajar con el valor absoluto para invertir los dígitos
while num > 0:
    digito = num % 10
    inverso = inverso * 10 + digito
    num //= 10

print("El inverso de los dígitos es:", inverso)
