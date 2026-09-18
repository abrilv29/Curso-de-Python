# Bucles son instrucciones que se van a repetir siempre y cuando la condicion sea Verdadera

i = 0

"""while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1""" # output: 1 2 3 4 5

"""while i <= 10:
    print(i)
    i += 1""" # output: 1 2 3 4 5 6 7 8 9 10

"""while i <= 10:
    i += 1
    print(i)""" # output: 2 3 4 5 6 7 8 9 10 11

# Iniciamos la variable i en 0
"""while i <= 10:
    i += 1
    print(i)""" # output: 1 2 3 4 5 6 7 8 9 10 11

"""while i <= 10:
    if i == 5:
        break
    i += 2
    print(i)""" #output: 2 4 6 8 10 12 
    
while i < 10:
      i += 1
      if i == 5:
       continue
      print(i) # output: 1 2 3 4 6 7 8 9 10
else: 
    print("i dejo de ser menor que 10")