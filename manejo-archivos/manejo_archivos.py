#open (nombre , modo)
# R read Lectura
# W write Escritura
# X crear archivos nuevos

#sin try 
"""f = open("archivo.txt","r")
print(f.readline())
f.close()
print("No se ha encontrado el archivo")
"""
"""try:
 f = open("archivo.txt","r")
 print(f.readline())
 f.close()
except FileNotFoundError:
 print("No se ha encontrado el archivo")"""

#uso del with y read
"""try:
 with open("archivo.txt","r", encoding="utf-8") as f:
  print(f.readline())
except FileNotFoundError:
 print("No se ha encontrado el archivo")"""

#uso del with y write
try:
 with open("archivo.txt","w") as f:
  print(f.write("Hola mundo desde write en el with"))
  with open("archivo.txt","r", encoding="utf-8") as f:
   print(f.readline())
except FileNotFoundError:
 print("No se ha encontrado el archivo")