#Colección de pares clave calor(Ordenado a partir de Python 3.7)
auto ={
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025
}

print(auto) #out: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2025}
print(auto["marca"]) #out: Renault
print(auto.get("marca"))#out: Renault

#Keys del diccionario
print(auto.keys())#out: dict_keys(['marca', 'modelo', 'año'])

#VALUES del diccionario
print(auto.values()) #out:dict_values(['Renault', 'Clio', 2025])

#SABER SI EXISTE UN VALOR
if "marca" in auto: 
    print("Marva es uno de los elementos de este diccionario")#out:Marva es uno de los elementos de este diccionario
else:
    print("Valor no encontrado") 
#out: Valor no encontrado si escribimos "Marca" con mayusculas
#caseSensity


#MODIFICAR UN VALUE
auto["año"] = 2020
print(auto) #out: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2020}

#AGREGAR VALUES
auto["color"] = "verde"
print(auto) #out: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2020, 'color': 'verde'}

#Elemento UPDATE | AGREGAR | MODIFICAR
auto.update({"año":2022, "puertas":4})
print(auto)#out: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2022, 'color': 'verde', 'puertas': 4}

"""#Eliminar elementos
auto.pop("puertas")
print(auto) #out: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2022, 'color': 'verde'}

#POPITEM: elimina el ultimo elemento del diccionario 
auto.popitem()
print(auto) #out: {'marca': 'Renault', 'modelo': 'Clio', 'año': 2022}

#CLEAR: limpia completamente el diccionario 
auto.clear()
print(auto) #out: {}
"""

#BUCLE FOR 
#Recorremos las keys 
for k in auto:
 print(k)
#out: marca modelo año color puertas
print("------------------------------------")
#Recorrer los values
for v in auto:
   print(v)
#out: marca modelo año color puertas
print("------------------------------------")
for v in auto.values():
   print(v)
#out: Renault Clio 2022 verde 4

print("------------------------------------")

"""for ambos in auto:
   len(auto)
   print(auto)"""

for k,v in auto.items():
    print(k, ":", v)
#Con auto.items() el bucle recorre cada par clave-valor una sola vez, no repite el diccionario completo en cada vuelta como pasaba antes.


#Dicicionarios Anidados 

familia = {
  "hijo1" :{
    "nombre":"Pedro",
    "edad": 8
  },
  "hijo2" :{
    "nombre":"Ana",
    "edad": 7
  },
  "hijo3" :{
    "nombre":"Marcelo",
    "edad":6
  }
}

print(familia)
#output: {'hijo1': {'nombre': 'Pedro', 'edad': 8}, 'hijo2': {'nombre': 'Ana', 'edad': 7}, 'hijo3': {'nombre': 'Marcelo', 'edad': 6}}

print(familia["hijo1"]["nombre"]) #out: Pedro