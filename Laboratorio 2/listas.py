#//////////////////////////////////////////
#//////////////////////////////////////////
#                 Listas
#//////////////////////////////////////////
#//////////////////////////////////////////


#=========================================
# Las listas pueden ser objetos diferentes
#-----------------------------------------
miPrimeraLista = [] #Lista vacía
print("Lista vacía: ", miPrimeraLista)


#=======================================
#  Llenando la lista
#---------------------------------------
miPrimeraLista = [1, "Javier", 3.14, True, "Fabiana"]
print("Lista nueva", miPrimeraLista)


#=======================================
#  list: hacer una lista
#  range(i,j): secuencia de i hasta j
#---------------------------------------
numeros = list(range(1, 61))

for i in numeros: 
    print(i)


#======================================
#  Incluir nuevos elementos en la lista
#--------------------------------------
numeros.append(63)
numeros.append(666)
numeros.append(63)
print("Lista agregando nuevos valores: ", numeros)


#======================================
# Quitar elementos de la lista
#--------------------------------------
numeros.remove(60)
print("#60 eliminado: ", numeros)


#======================================
# Quitar elemento con índice i
#--------------------------------------
i = 1
del numeros[i]    
print("Nuevos elementos: ", numeros)
                  # NO ELIMINA EL 1 DE LA LISTA ):
                  # ¿POR QUÉ?


#=====================================
# Borrar la lista
#-------------------------------------
del numeros
# Si escribimos "print (numeros)" nos marcará error, 
# porque ya la habrá eliminado.


#===================================
# Sumar listas
#-----------------------------------
L1 = [1,2,3]
L2 = [4,5,3]
print("L1 + L2 = ", L1+L2)


#=================================
# Llenado a mano
#--------------------------------
potencial = []  #Lista vacía
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])  # Agrega "100" a la lista vacía
                       # El numero que agregamos debe estra dentro del rango


#==================================
# Generar una tupla con la lista
#----------------------------------
potencial = tuple(potencial)
print(potencial[6])


