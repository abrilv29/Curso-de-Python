#Conjunto(set):Colecciones no ordenadas de elementos únicos(no se puede acceder por índices)
frutas = {"Manzana","Naranja","Mandarina","Naranja"}
print(frutas) #out: {'Manzana', 'Mandarina', 'Naranja'}
print(type(frutas)) #out: <class 'set'>
print(len(frutas)) #out: 3 No se toma encuenta los duplicados

"""conjunto = {"Python",156,True}
print(conjunto) #out: {True, 156, 'Python'}
print(type(conjunto)) #out:<class 'set'>

for item in conjunto:
    print(item) #out: True 156 Python
#No necesariamente te muestra los elementos ordenados """


#IN: sirve para revisar si el elemento esta dentro del conjunto
print("Manzana" in frutas) #out:True
print("Pera" not in frutas) #out:True

#ADD: agregar elementos al conjunto
frutas.add("Pera")
print(frutas) #out: {'Mandarina', 'Naranja', 'Manzana', 'Pera'}

#UPDATE: agregar mas de un elemento al conjunto
frutasTropicales = {"Piña","Mango"} #agregar lsitas,tuplas,conjuntos
frutas.update(frutasTropicales)
print(frutas) #out: {'Manzana', 'Piña', 'Mango', 'Pera', 'Naranja', 'Mandarina'}

#REMOVE:eliminar elementos dentro del conjunto
frutas.remove("Mango")
print(frutas) #out: {'Manzana', 'Pera', 'Naranja', 'Piña', 'Mandarina'}
#Discard: borra el elemento dentro del conjunto, pero si este no existe no nos mandara un error, solo ignorara la instrucción 
frutas.discard("Banana")
print(frutas) #out: {'Naranja', 'Mandarina', 'Piña', 'Pera', 'Manzana'}

frutas.discard("Pera")
print(frutas) #out:{'Piña', 'Naranja', 'Mandarina', 'Manzana'}

#Pop: elimina elementos dentro del conjunto al azar 
frutas.pop()
print(frutas) #out: {'Naranja', 'Piña', 'Mandarina'}

#Clear: Vacíar el conjunto
frutas.clear()
print(frutas) #out: set()

print("----------------------------------------")

#Operaciones entre conjuntos

a = {"a","b","c"}
b = {"c","d","e"}

#Union de conjuntos AB
#No toma el elemento duplicado solo toma uno en este caso la "c"
c = a.union(b)
print(c) #out: {'b', 'a', 'd', 'c', 'e'}

#Elementos en común AB
#Elemento que coincidan o tenga en comun a y b
i = a.intersection(b)
print(i) #out: {'c'}

#Diferencia entre AB
#Elementos que esten en a pero no en b
d = a.difference(b)
print(d) #out: {'a', 'b'}
