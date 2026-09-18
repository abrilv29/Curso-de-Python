# Operadores de comparacion 

x = 5
y = 3
z = 5

print(x == y) #si es igual false
print( x != y) #si es distinto True
print(x > y) #es mayor True
print(x < y ) #es menor False
print(x >= z)# es mayor o igual True
print(x <= y)#es menor o igual false



# Operadores Logicos

# AND = todas la condiciones deben ser true

#     True      False
print(x > y and y > z) # False

# OR = con que una de las condiciones se cumpla te puede dar true

print(x > y or y > z) # True

# Negar condiciones 

v = True
f = False

print(not(v))
print(not(f))