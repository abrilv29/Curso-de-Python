#Los modulos usan el import para traerte la logica que esta en otro archivo 
"""import operaciones
print(operaciones.suma(2,3)) #out:5"""
#import: trae el archivo completo dentro de su modulo
#from: importa una funcion sin prefijo de módulo
#import multiple: importa varias funciones separadas, por coma
#modulo.funcion: accede a una funcion dentro de su modulo
from operaciones import suma,resta,multiplicacion,division
print(suma(2,3)) #out:5
print(resta(2,3))
print(multiplicacion(2,3))
print(division(10,5))


