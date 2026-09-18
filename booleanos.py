# valores booleanos que pueden tomar True o False
verdadero = True
falso = False
print(verdadero)
print(falso)

print(5>3)  #Verdadero
print(5<3)  #Falso

print(type(verdadero))  #Tipo de dato booleano
print(bool("Hola Mundo"))  #Convertir a booleano
print(bool(""))  #Convertir a booleano

#TRUE 

print(bool("abcd"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


#FALSE

print(bool(""))
print(bool(0))
print(bool(None))
print(bool([]))

x = 123
print(isinstance(x, int))  #True enteros
x = 123.5
print(isinstance(x, int))  #False enteros