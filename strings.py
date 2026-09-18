# Declaracion de cadenas de texto (Strings)
print("Hola,'Mundo!'")

ingles = "I'm learning Python"

multiples = """Esto es una cadena de texto
que ocupa multiples lineas"""

print(ingles)
print(multiples)


#Metodo length() para obtener la longitud de una cadena de texto
print(len(ingles))
print(len(multiples))

texto = "Este curso es de fundamentos de Python"
estaIncluida = "Python" in texto # saber si el texto esta incluido 
print(estaIncluida)
# Si influye la mayuscula o minuscula en la busqueda de una cadena de texto

noEstaIncluida = "JavaScript" not in texto
print(noEstaIncluida) #Saber si el texto no esta incluido

# Convertir a mayusculas o minusculas una cadena de texto
mayusculas = "ESTO ES UNA CADENA DE TEXTO EN MAYUSCULAS"
minusculas = "esto es una cadena de texto en minusculas"

print(minusculas.upper())
print(mayusculas.lower())

# texto.upper() # Convertir a mayusculas
# texto.lower() # Convertir a minusculas


# Espacio al inicio y al final de una cadena de texto

espacios = "   Esto es una cadena de texto con espacios al inicio y al final   "
sinEspacios = espacios.strip() # Eliminar espacios al inicio y al final de la cadena de texto
print(sinEspacios)

# Cortar una cadena de texto en partes
#indice 0 = siempre comienza en 0
#        0123 45 67 891011
texto = "Este es un texto de ejemplo"
print(texto[0]) # E
print(texto[5]) # e 

# Posicion de palabras en una cadena de texto
# Alcontar una cadena de texto,tambien incluye los espacios en blanco
print(texto[0:4]) # Este
print(texto[11:16]) # texto
print(texto[20:27]) # ejemplo


# Remplazar una cadena de texto por otra
texto = "Este es un curso de JavaScript"
texto = texto.replace("JavaScript", "Python")
print(texto)

#Dividir una cadena de texto en partes
textoDividido = texto.split(" ") # Dividir la cadena de texto en partes, separadas por espacios
print(textoDividido) # ['Este', 'es', 'un', 'curso

#Normalizacion de cadenas de texto
texto2 = "Este texto tiene MAYUSCULAS y minisculas y necesito encontrar ciertas palabras"
print("mayusculas" in texto2.lower()) # Normalizar a minusculas y buscar la palabra