# Bucle for 
palabra = "Python"
for letra in palabra:
    print(letra) # output: P y t h o n

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    if fruta == "banana":
        continue #output: manzana cereza
        # break #output: manzana
    print(fruta)
else:
    print("No hay mas frutas en la lista") #output: No hay mas frutas en la lista


# Elementos del for
# item = itera cada elemento de la lista manzana, banana, cereza
# items = itera el listado completo en este caso frutas


print("-------------------------------------")

#Rango de numeros
#Comienza desde el cero y termina en el numero que se asigno sin incluirlo
"""for i in range(10):
    print(i) # output: 0 1 2 3 4 5 6 7 8 9"""

"""for i in range(3,5):
    print(i) # output: 3 4"""

"""for i in range(0, 10, 2):
    print(i) # output: 0 2 4 6 8"""


#Bucles anidados 

adjetivos = ["Rica","Saludable"]
frutas = ["manzana", "banana", "cereza"]

"""for adjetivo in adjetivos:
    for fruta in frutas:
        print(adjetivo, fruta) # output: 
        #Rica manzana 
        #Rica banana 
        #Rica cereza 
        # Saludable manzana 
        # Saludable banana 
        # Saludable cereza"""

# intercalar los elementos de dos listas
for fruta in frutas:
    for adjetivo in adjetivos:
        print(adjetivo, fruta)
        # output:
"""        Rica manzana
           Saludable manzana
           Rica banana
           Saludable banana
           Rica cereza
           Saludable cereza"""

# Nota: recuerda que el orden de las listas afecta el resultado del bucle anidado. En este caso, se imprimen todos los adjetivos para cada fruta.