#Ejercicio 1 

print("Hola Mundo!")

#Ejercicio2

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}!")

#Ejercicio 3

nomb = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar = input("Ingrese su lugar de residencia: ")

print(f"Me llamo {nomb} {apellido}, tengo {edad} años y vivo en {lugar}.")

#Ejercicio 4
import math 

radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área es: {area}")
print(f"El perímetro es: {perimetro}")

#Ejercicio 5
segundos = float(input("Ingrese la cantidad de segundos: "))

horas = round(segundos / 3600, 2)

print(f"el equivalente en horas son {horas} horas.")

#Ejercicio 6
numero_para_multiplicar = int(input("ingrese un numero entero para saber su tabla: "))

numero_0 = numero_para_multiplicar * 0
numero_1 = numero_para_multiplicar * 1
numero_2 = numero_para_multiplicar * 2
numero_3 = numero_para_multiplicar * 3
numero_4 = numero_para_multiplicar * 4
numero_5 = numero_para_multiplicar * 5
numero_6 = numero_para_multiplicar * 6
numero_7 = numero_para_multiplicar * 7
numero_8 = numero_para_multiplicar * 8
numero_9 = numero_para_multiplicar * 9
numero_10 = numero_para_multiplicar * 10

print(f"""
  {numero_para_multiplicar} x 0 = {numero_0}
  {numero_para_multiplicar} x 1 = {numero_1}
  {numero_para_multiplicar} x 2 = {numero_2}
  {numero_para_multiplicar} x 3 = {numero_3}
  {numero_para_multiplicar} x 4 = {numero_4}
  {numero_para_multiplicar} x 5 = {numero_5}
  {numero_para_multiplicar} x 6 = {numero_6}
  {numero_para_multiplicar} x 7 = {numero_7}
  {numero_para_multiplicar} x 8 = {numero_8}
  {numero_para_multiplicar} x 9 = {numero_9}
      """)

#Ejercicio 7
numero_a = input("Ingrese un número distinto a 0: ")
numero_b = input("Ingrese otro número distinto a 0: ")

suma_a_b = int(numero_a) + int(numero_b)
resta_a_b = int(numero_a) - int(numero_b)
multiplicacion_a_b = int(numero_a) * int(numero_b)
division_a_b = int(numero_a) / int(numero_b)

print(f"""
La suma de {numero_a} y {numero_b} es: {suma_a_b}
La resta de {numero_a} y {numero_b} es: {resta_a_b}
La multiplicación de {numero_a} y {numero_b} es: {multiplicacion_a_b}
La división de {numero_a} y {numero_b} es: {division_a_b}
""")

#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))  

imc = peso / (altura ** 2)

print(f"Su índice de masa corporal (IMC) es: {imc}")

#Ejercicio 9
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))    
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")