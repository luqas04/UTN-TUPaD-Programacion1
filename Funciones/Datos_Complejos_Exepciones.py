menu = 0
while True:
    try: 
        espacios = int(input("Ingrese la cantidad de espacios que desea que tenga su mochila: "))
        if espacios > 0:
            mochila = []
            for i in range(espacios):
                mochila.append("--vacio--")
            break
        else:
            raise ValueError

    except ValueError:
        print("Debe ingresar un numero entero positivo")
        continue


while menu != 3:
    print("---Menu de la Mochila---")
    print("Opcion 1. Guardar Obejeto")
    print("Opcion 2. Ver Mochila")
    print("Opcion 3. Salir")

    try:
        menu = int(input("Ingrese una Opcion: "))
    except ValueError:
        print("Debe ingresar un numero no letras")
        continue

    if menu == 1:
        print("--Esto es lo que tiene la mochila ahora mismo---")
        print(mochila)

        try: 
            posicion = int(input("Que espacio desea cambiar: "))
            if posicion < 0 or posicion >= len(mochila):
                raise IndexError
            else:
                mochila[posicion] = input("Que va a guardar en ese espacio: ")
                print("Objeto guardado con exito")
        except ValueError:
            print("Debe ingresar un numero")
        except IndexError:
            print("Ese espacio no existe en la mochila o es un numero negativo")
    elif menu == 2:
        print("---Esto es lo que tiene la mochila ahora mismo---")
        print(mochila)
    elif menu == 3:
        break
    else:
        print("Debe ingresar una opcion valida")



        

