#Función: es un bloque de código que solo se ejecuta cuna lo llamamos.
#Permite organizar y modularizar el código(reutilización)

# acronimo def se usa para declar una función 
#ARGUMENTO: es la variable que espera la funcion ejemplo:nombre
#Parametro: el valor que le pasamos a la función ejempo:Abril
def saludar(nombre,apellido): #argumentos
    print("Hola",nombre,apellido)
saludar("Abril","Vargas") #Parametros
#out: Hola Abril Vargas


#Podemos agerar un argumento por default,
def saludo(nombre,nacionalidad="Mexicana"):
    print("Hola",nombre,nacionalidad)
saludo("Abril","Colombia")
saludo("kenia")
#out:
"""Hola Abril Colombia
Hola kenia Mexicana"""

def sumar(a,b):
    return a+b
resultado = sumar(10,20)
print(resultado)

def funcion():
    pass
#Declarar la funcion vacia, si aun no esta definida


def restar(a,b):
    return a-b
res = restar(20,10)
print(res)

def multiplicar(a,b):
    return a*b
resM = multiplicar(20,10)
print(resM)

def dividir(a,b):
     return a/b
resD= dividir(20,10)
print(resD)






