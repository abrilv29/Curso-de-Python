# LISTAS: las listas son ordenadas,modificables y permiten valores duplicados.

#indice:    0          1           2
frutas = ["manzana", "naranja", "mandarina"]
print(frutas) # output: ['manzana', 'naranja', 'mandarina']
print(type(frutas)) # output: <class 'list'>

#Listas: sustituir un valor de la lista
frutas[1] = "pera" # modificamos el valor de la lista en el indice 1
print(frutas) # output: ['manzana', 'pera', 'mandarina']

#Listas con valores mixtos
lista = ["Abril Vargas",5,True]
print(lista) # output: ['Abril Vargas', 5, True]
print(type(lista)) # output: <class 'list'>
print("La lista mixta tiene", len(lista), "elementos") # output: 3

#Lista: rango de indices
print(frutas[0:2]) # output: ['manzana', 'pera']
print(frutas[1:]) # output: ['pera', 'mandarina']

#Lista: saber si un elemento esta en la lista
if "pera" in frutas:
    print("Si, la pera esta en la lista") #out: si, la pera esta en la lista
else:
    print("No, la pera no esta en la lista")


#Lista: Metodos para modificar la lista
#append: agrega un elemento al final de la lista
#indices      0        1      2
vehiculos = ["auto", "moto","avión"] 
vehiculos.append("barco") #3
print(vehiculos) # output: ['auto', 'moto', 'avión', 'barco']

#Insert: agrega un elemento en el indice que le indiquemos
vehiculos.insert(1,"bicicleta")
print(vehiculos) # output:['auto', 'bicicleta', 'moto', 'avión', 'barco']

#Remove: elimina un elemento de la lista
vehiculos.remove("auto")
print(vehiculos) # output: ['bicicleta', 'moto', 'avión', 'barco']

#Pop: elimina un elemento de la lista en el indice que le indiquemos
vehiculos.pop(1)
print(vehiculos) # output: ['bicicleta', 'avión', 'barco']

#sort: ordena la lista de menor a mayor
vehiculos.sort()
print(vehiculos) # output: ['avión', 'barco', 'bicicleta']

#reverse: invierte el orden de la lista
vehiculos.reverse()
print(vehiculos) # output: ['bicicleta', 'barco', 'avión']

#Unir listas: extend: agrega los elementos de una lista a otra lista
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]
coleccion1.extend(coleccion2)
print(coleccion1) # output: [1,2,3,4,5,6]

#coleccion3 = coleccion1 + coleccion2
#print("Las colecciones unidas son:", coleccion3) # output: [1,2,3,4,5,6]