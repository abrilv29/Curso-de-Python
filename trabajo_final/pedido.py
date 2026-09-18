#DECLARAR EL ARCHIVO COMO CONSTANTE

ARCHIVO_PEDIDOS = "pedidos.txt"

def pedido_cafe():
    print("\n Elige el café que prefieras")
    print("1. Expresso")
    print("2. Capuchino")
    print("3. ChaiLate")
    print("4. Americano")

    opcion = input("Opción: ")

    cafes = {
        "1": "Expreso",
        "2": "Capuchino",
        "3": "ChaiLate",
        "4": "Americano"
    }

    if opcion  in cafes:
     cafe_elegido = cafes[opcion]
     print("Has pedido un" + " " + cafe_elegido + ". 'Preparando tu café!'")
     #Crear el archivo del menú
     with open(ARCHIVO_PEDIDOS, "a", encoding= "utf-8") as archivo:
       archivo.write(cafe_elegido + "\n")
    else:
     print("La opción no es válida, por favor intenta de nuevo")
