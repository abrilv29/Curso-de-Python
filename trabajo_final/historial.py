ARCHIVO_PEDIDOS = "pedidos.txt"
def ver_historial():
    try:
        print("\n Historial de pedidos")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i,pedido in enumerate(pedidos, start=1):
                    print(str(i)+" . "+ pedido.strip())
            else:
                print("Aún no hay pedidos")            
    except FileNotFoundError:
        print("\n Todavía no existe un historial de pedidos")


"""
readline() → una sola línea (string)
readlines() → todas las líneas (lista de strings)
read() → todo el archivo entero (un solo string, sin dividir por líneas)
"""