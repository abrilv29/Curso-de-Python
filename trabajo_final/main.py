from menu import mostrar_menu
from pedido import pedido_cafe
from historial import ver_historial

def main():
    while True:
        #Mostrar el menú del café 
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        match opcion:
            case "1":
                #pedir un cafe
                pedido_cafe()
            case "2":
                #ver el historial
                ver_historial()
            case "3": 
                print("\n Muchas gracias por haber tomado nuestro riquism0o café")
                break
            case _:
             print("Opción inválida, por favor indique una de las opciones siguientes")


if __name__ == "__main__":
    main()

"""
El if __name__ == "__main__": es la manera de asegurar que un archivo no se "autoejecute" 
cuando otro lo está importando — solo se ejecuta cuando tú lo corres directamente.
"""