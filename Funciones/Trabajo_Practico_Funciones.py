import math
#Ejercicio 1: Crear una función que imprima "Hola Mundo" en la consola.

def hola_mundo():
    print("Hola Mundo")

hola_mundo()

#Ejercicio 2: Crear una función que reciba un nombre como parámetro y salude a esa persona.

def saludar(nombre):
    print(f"Hola, {nombre}!")

nombre_usuario = input("Ingrese su nombre: ")
saludar(nombre_usuario)

#Ejercicio 3: Crear una función que muestra la informacion personal.

def informacion_personal(nombre, edad, ciudad):
    print(f"Hola soy {nombre}, tengo {edad} años y vivo en {ciudad}.")

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad: ")
informacion_personal(nombre, edad, ciudad)

#Ejecicio 4: Crear una Funcion que calcule el area de un circulo.

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area


radio = float(input("Ingrese el radio del circulo en este formato(0.0): "))
area = area_circulo(radio)
print(f"El área del círculo es: {area}")

#Ejercicio 5: Funcion que convierta segundos a horas:

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas.")

#Ejercicio 6: funcion que crea la tabla de multiplicar de un numero.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio 7: Funcion de operaciones basicas.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (no se puede dividir por cero)"
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

input_a = float(input("Ingrese el primer número: "))
input_b = float(input("Ingrese el segundo número: "))   
operaciones_basicas(input_a, input_b)


#Ejercicio 8: Funcion que calcula el IMC.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos (ejemplo 70.5): "))
altura = float(input("Ingrese su altura en metros (ejemplo 1.75): "))   
imc = calcular_imc(peso, altura)
print(f"Su Índice de Masa Corporal (IMC) es: {imc}")


#Ejercicio 9: Funcion que convierta grados Celsius a Fahrenheit.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

#Ejercicio 10: Funcion que calcula promedio de tres numeros.

def calcular_promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")

