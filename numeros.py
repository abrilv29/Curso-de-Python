# Tipos de numeros 
# enteros, decimales y complejos

# enteros
x = 1

#decimales
y = 2.8

#complejos estan compuestos de real e imaginario, se representan con la letra j
z = 1j

print(type(x))
print(type(y))
print(type(z))


#conversion de tipos de numeros

xf= float(x) #convertir a decimal
print(xf)
print(type(xf))

ye = int(y) #convertir a entero
print(ye)
print(type(ye))

ze = complex(x) #convertir a complejo
print(ze)
print(type(ze))


#Numeros aleatorios
import random
print(random.randrange(1, 10))# numero aleatorio del 1 al 9

