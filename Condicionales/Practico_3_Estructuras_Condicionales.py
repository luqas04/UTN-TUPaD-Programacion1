from statistics import mode, median, mean
import random

# Ejercicio 1: Verificar si el usuario es mayor o menor de edad

edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Edad no válida")
elif edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad") 

# Ejercicio 2: Verificar si la nota esta aprobada

nota = int(input("Ingrese su nota (0-10): "))

if nota < 0 or nota > 10:
    print("Nota no válida")
elif nota < 6:
    print("Nota desaprobada")
else:
    print("Nota aprobada")

# Ejercicio 3: Verificar si un número es par o impar

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("El número es par") 
else:
    print("El número es impar")

# Ejercicio 4: Verificar a que grupo pertenece una persona según su edad

edad_grupo = int(input("indica tu edad: "))

if edad_grupo < 0:
    print("Edad no válida")
elif edad_grupo < 12:
    print("Eres un niño")
elif edad_grupo < 18:
    print("Eres un adolescente")
elif edad_grupo >= 18 and edad_grupo < 30:
    print("Eres un adulto/joven")
else:
    print("Eres un adulto/mayor")

# Ejercicio 5: Verificar si la contraseña es correcta

contraseña = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

if len(contraseña) < 8:
    print("Contraseña demasiado corta")
elif len(contraseña) > 14:
    print("Contraseña demasiado larga")
else:
    print("Contraseña válida")

#ejercicio 6: calcular la moda, mediana y media de una lista de números

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

mode(numeros_aleatorios)
median(numeros_aleatorios)
mean(numeros_aleatorios)

print("Lista de números aleatorios:", numeros_aleatorios)

if (mean > median) and (mean > mode):
    print("sesgo a positivo")
elif (mean < median) and (mean < mode):
    print("sesgo a negativo")
elif (mean == median) and (mean == mode):
    print("sin sesgo")


# Ejercicio 7: Anadir un signo de exclamación a una frase si termina en vocal

frase = input("Ingrese una frase: ")

if frase[-1].lower() in 'aeiou':
    frase += '!'
    print("Frase modificada:", frase)
else:
    print("Frase sin cambios:", frase)

# Ejercicio 8: Convertir su nombre a mayúsculas o minusculas

nombre_usuario = input("Ingrese su nombre: ")
menu = True
while menu:
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    print("3. Convertir solo la primera letra a mayúscula")

    input_usuario = int(input("Seleccione una opción (1-3): "))

    if input_usuario == 1:
        print("Nombre en mayúsculas:", nombre_usuario.upper())
        menu = False
    elif input_usuario == 2:
        print("Nombre en minúsculas:", nombre_usuario.lower())
        menu
    elif input_usuario == 3:
        print("Nombre con primera letra en mayúscula:", nombre_usuario.capitalize())
        menu = False
    else:
        print("Opción no válida, intente de nuevo.")
    
# Ejercicio 9: clasificar magnitud de un terremoto

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 0:
    print("Magnitud no válida")
elif magnitud < 3.0:
    print("Muy leve, imperceptible")
elif magnitud >= 3.0 and  magnitud < 4.0:
    print("Leve, ligeramente perceptible")
elif magnitud >= 4.0 and magnitud < 5.0:
    print("Moderado, se puede sentir pero no causa daños")
elif magnitud >= 5.0 and magnitud < 6.0:
    print("Fuerte, puede causar daños menores")
elif magnitud >= 6.0 and magnitud < 7.0:
    print("Muy Fuerte, puede causar daños severos en áreas pobladas")
elif magnitud >= 7.0:
    print("Extremo, puede causar daños graves en áreas extensas")

# Ejercicio 10: imprimir su estacion dependiendo del hemisferio y la fecha

hemisferio = input("Ingrese su hemisferio (Norte/Sur): ").strip().lower()

mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio not in ['norte', 'sur']:
    print("Hemisferio no válido")
elif mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Fecha no válida")
else:
    if hemisferio == 'norte':
        if (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
            print("Es invierno")
        elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
            print("Es primavera")
        elif (mes == 6 and dia >= 21) or (mes <= 9 and dia < 23):
            print("Es verano")
        elif (mes == 9 and dia >= 23) or (mes <= 12 and dia < 21):
            print("Es otoño")
    else:  # hemisferio sur
        if (mes == 6 and dia >= 21) or (mes <= 9 and dia < 23):
            print("Es invierno")
        elif (mes == 9 and dia >= 23) or (mes <= 12 and dia < 21):
            print("Es primavera")
        elif (mes == 12 and dia >= 21) or (mes <= 3 and dia < 20):
            print("Es verano")
        elif (mes == 3 and dia >= 20) or (mes <= 6 and dia < 21):
            print("Es otoño")



