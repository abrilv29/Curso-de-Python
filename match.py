# Sentencia Match es como usar un switch case en otros lenguajes de programación, pero con más funcionalidades y más potente.
dia = 1

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Día no válido")

frutas = "banana"
match frutas:
    case "manzana":
        print("manzana roja")
    case "pera":
        print("pera verde")
    case "banana":
        print("platano dominico")
    case "naranja":
        print("naranja dulce")
    case _:
        print("No es una fruta válida")