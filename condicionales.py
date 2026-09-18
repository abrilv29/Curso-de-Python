# IF,ELSE
# 1.- Python evalua el orden de  arriba hacia abajo
# 2.- Con los if anidados busca el primer TRUE, que cumpla con la condicion y ya no ejecuta las demas condiciones


x = 5
y = 3

"""if x > y:
    print("x es mayor a y") # output: 5 es mayor a 3
elif x == y:
    print("x es igual a y") # output: 5 es igual a 3
else:
    print("Ninguna de las anteriores se cumplio")"""


# ejemplo 2 and | or | not 
z = 10

if x > y and x > z:
    print("x es mayor a y y z")
elif x == y or x == z:
    print("x es igual a y o z")
else:
    print("Ninguna de las anteriores se cumplio")


a = "Python"
b = "JavaScript"
c= "Python"
if a == c:
    print("a es igual a b")
    if a == b:
     print("a es igual a c") # output: a es igual a c
    else: 
     print("Estoy saliendo por el else del if interno")
else:
    print("a no es igual a b") # output: a es diferente a b


e = 10
f = 10

if e == f:
   pass # placeholder temporal sin romper la ejecución