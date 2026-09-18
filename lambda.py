#Funcion pequeña, y anonima que puede tener argumentos pero sólo una expresión

#Sintaxix lambda argumentos: expresión 

"""x = lambda a: a + 10
print(x(5)) #out: 15 a vale 5"""

"""x = lambda a, b  : a + b
print(x(2,3)) #out: 5"""

def mifuncion(n):
    return lambda a: a* n
duplicador = mifuncion(2)
triplicador = mifuncion(3)
cuatriplicador = mifuncion(4)
quintuplicador = mifuncion(5)
print(duplicador(5)) #out:10 5*2
print(triplicador(5)) #out: 15 5*3
print(cuatriplicador(5)) #out:20 5*4
print(quintuplicador(5))#out: 25 5*5


