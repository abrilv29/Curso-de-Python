#Colecciones ordenadas e inmutables(NO SE PUEDEN MODIFICAR)
#Tuplas
#indice:         0          1      2
tecnologias = ("Python", "Java", "C++","Python") #Las tuplas pueden tener elementos duplicados
print(tecnologias) # output: ('Python', 'Java', 'C++')
print(tecnologias[2]) # output: Python
print(len(tecnologias)) # output: 4
print(type(tecnologias)) # output: <class 'tuple'>

frutas = ("manzana",)
print(type(frutas)) # output: <class 'str'>, porque no es una tupla, es un string

tupla=("Python",5,True)
print(tupla) # output: ('Python', 5, True)
print(type(tupla)) # output: <class 'tuple'>

#Desempaquetar tuplas

x,y,z = tupla
print(x)
print(y)
print(z) #out: True

#Unir tuplas
tupla1 = (1,2,3)
tupla2 = (3,4,5)
tupla3=tupla1+tupla2
print(tupla3) #out: (1, 2, 3, 3, 4, 5)
print("---------------------------------------------")
#Duplicar tuplas
print(tupla*2) #out:('Python', 5, True, 'Python', 5, True)

print("---------------------------------------------")
#Recorer una tupla con el bucle for 
for item in tupla:
    print(item) #out: Python,5,True

print("---------------------------------------------")

#Convertir la tupla en lista y volverla a convertirla 
#Tupla a modidicar
tuplaModidicada = ("Python","JavaScript","Go")
listaComodin = list(tuplaModidicada)
print(listaComodin)
listaComodin.append("ReactJS")
tuplaModidicada = tuple(listaComodin)
print(tuplaModidicada)


