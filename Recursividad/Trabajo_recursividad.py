# Ejercicio 1: Factorial de un número usando recursividad

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Ejercicio 2: Serie de Fibonacci usando recursividad

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Ejercicio 3: potencia de un número usando recursividad

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
# Ejercicio 4: pasaje a binario usando recursividad

def a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return a_binario(n // 2) + str(n % 2)
    

# Ejercicio 5: Reconocer si una palabra es un palíndromo usando recursividad

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
# Ejercicio 6: Suma de los dígitos de un número usando recursividad
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
# Ejercicio 7: Problema del niño y los bloques usando recursividad

def contar_bloques(n):
    if n == 0:
        return 1
    else:
        # Llamada recursiva para contar los bloques restantes
        return contar_bloques(n - 1) + n

# Ejercicio 8: Contador de digitos en un número usando recursividad

def contar_digito(numero,digito): # Contar cuántas veces aparece un dígito en un número
    if numero == 0:
        return 0
    #   Caso base: si el número es 0, no hay dígitos que contar
    else:
        # Verificar si el último dígito es igual al dígito buscado
        cuenta = 1 if numero % 10 == digito else 0
        # Llamada recursiva para el siguiente dígito
        return cuenta + contar_digito(numero // 10, digito)
    
