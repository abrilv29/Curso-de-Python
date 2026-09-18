#Manejo de errores
try:
    numero = 10/0
except ZeroDivisionError:
    print("No se puede divir por cero")

try:
    print(x)
except NameError:
    print("Esta variable no esta definida")
finally:
    print("Esto sera ejecutado siendo exitoso o no el bloque")