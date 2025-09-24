# Ejercicio 1

numeros_1_100 = []

for i in range(0,101,4):
    numeros_1_100.append(i)

print(numeros_1_100)

#Ejercicio 2

lista_1 = ["Alonso","Verstappen","Hamilton","Colapinto","Piastri"]

print(lista_1[-3])

#Ejercicio 3

lista_vacia = []

lista_vacia.append("Hola")
lista_vacia.append("Chau")
lista_vacia.append("Adios")

print(lista_vacia)

#Ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]

print(animales)

animales[1] = "loro"
animales[-1] = "oso"

print("---Despues del cambio---")
print(animales)

#Ejercicio 5

#Ese programa lo que hace es quitar el numero mas alto de la lista "numeros", en este caso el "22"
#numeros = [8,15,3,7]

#Ejercicio 6

lista_2 = []

for i in range(10,31,5):
    lista_2.append(i)

print(lista_2[0],lista_2[1])

#Ejercicio 9

autos = ["sedan", "polo", "suran", "gol"] 

autos[1] = "Porsche"
autos[2] = "BMW"

print(autos)


#Ejercicio 8

dobles = []

for i in range(5,16,5):
    dobles.append(i*2)

print(dobles)

#Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]] 

compras[2].append("jugo")

compras[1][1] = "Tallarines"

compras[0].remove("pan")

print(compras)

#Ejercicio 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)


