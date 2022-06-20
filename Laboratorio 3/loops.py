#========================================#
#                                        #
#               CONDICIONALES            #
#                                        #
#========================================#

precio = 50

#---------------
#Si pasa esto...
#---------------
if precio < 50:
  print("El precio es menor que 50")

#------------------------------
# Si no... si pasa esto otro...
#------------------------------
elif precio > 50:
    print("El precio es mayor a 50")

#-----------------------------------
# Si no pasa nada de lo anterior....
#-----------------------------------
else:
    print("El precio es 50")

precio = 50
cantidad = 5
total = precio*cantidad

#============================
# Condicionales anidados
#----------------------------
if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("El total es menor que 500 y menor que 400")
        elif total < 500 and total > 300:
            print(" EL total es menor que 500 y mayor que 300")
        else:
            print("Total entre 100 y 300")

#=======================================
# El condicional de igualdad es ==
#---------------------------------------
elif total == 100:
    print("Total es 100")
else:
    print("Total es menor que 100")

#=============================================
# Contador mientras la condición sea verdadera
#---------------------------------------------
num = 0
while num < 5:
    num = num + 1
    print('num = ', num)

num = 0
while num < 5:
    num += 1    #num +=1 es lo mismo que num = num +1
    print("num = ", num)
    if num == 3:    # Condicional antes de salir del bucle
        break

num = 0
while num < 5:
    num += 1
    if num > 3:
       continue    #Evitar lo que sigue continuar con las iteraciones es
    print("num = ", num)

#===========================
#  Bucle sobre la lista
#---------------------------
num = [10, 20, 30, 40, 50]
for i in num:
    print(i)

#===========================
#  Bucle sobre un string
#---------------------------
for char in "Hello":
    print(char)

#==================================
#  Bucle sobre sobre un diccionario
#  items = elementos
#----------------------------------
numNames = {1:"uno", 2:"dos", 3:"tres"}
for pair in numNames.items():
    print(pair)

#=================================
#  Bucle sobre diccionario
#  key = llave
#  value = valor 
#--------------------------------
for k,v in numNames.items():
    print("key = ", k, ", value = ", v)






