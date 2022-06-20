#========================================#
#                                        #
#            CONJUNTO EN PYTHON          #
#                                        #
#========================================#


even_nums = {2, 4, 6, 8, 10} #Conjunto de números pares
print(even_nums)

# El bool no es parte del conjunto
emp = {1, 'Steve', 10.5, True} #Conjunto de diferentes objetos
print(emp)

nums = {1, 2, 3, 4, 4, 5, 5}
print(nums)

#=====================================
#    Convetir secuencia a conjunto
#    No lo genera en orden
#-------------------------------------  
s = set('Hello')
print(s)
s = set((1, 2, 3, 4)) #Tupla a conjunto
print (s)

#===============================================
#  De diccionario a conjunto:conjunto de llaves
#-----------------------------------------------

d = {1: 'One', 2: 'Two'}
s = set(d)
print (s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 #Unión
print(su)

si = s1&s2 #Intersección 
print(si)

sr = s1-s2 #DIferencia de conjuntos
print(sr)

sp = s2-s1
print(sp)

ss = s1^s2 #Diferencia simétrica
print(ss)

#==================================
#	Uso de diccionarios
#----------------------------------

Capitales = {"USA": "Washington D.C", "Francia":"Paris", "India":"Nueva Delhi"}
print(Capitales)

#=================
#   Llave:valor
#-----------------

d = {} # Diccionario vacío

# Llave entera, valor string
numNames={1:"One", 2:"Two", 3:"Three"}

# Llave real, valor string
decNames={1.5:"Uno punto cinco", 2.3:"Dos punto tres", 3.0:"Tres punto cero"}

# Llave tupla, valor string
items={("Fabiana", "Sandy", "Nayibi"):"amores", ("Javier", "Alejandro"):"Enamorado"}

# Llave string, valor int
NumRomanos={ 'I':1, 'II':2, 'III': 3, 'IV':4, 'V':5 }
print(NumRomanos)
print(NumRomanos["I"])
print(NumRomanos['I'])  # También puede ser con comillas simples
 
# Ejemplo que pones un país e imprime su capital

print(Capitales.get("India"))
print(Capitales.get("india"))
print(Capitales["USA"])

# Reportar llave y valor
for k in Capitales:
	print("Key = " + k + ", Value = " + Capitales[k])

# Agregar nuevo dato para el diccionario

Capitales["México"]= "CDMX"
print(Capitales)

# Borrar solo un dato  del diccionario
del Capitales["México"]
print("Capitales actualizadas : ", Capitales)

# Borrar todo  el diccionario
del Capitales
# print("Capitales actualización 2: ", Capitales)  # Esto marcará un error, porque no stá definido pq se borró

# Reportar llaves 
print(NumRomanos.keys()) #Imprime lo que va antes de dos puntos

#Reportar valores
print(NumRomanos.values()) #imprime lo que va después de los dos puntos

#Juicio de llave (está o no está la llave en el diccionario) Devuelve Fasle o True
print("I" in NumRomanos)
print("X" in NumRomanos)
print("1" in NumRomanos)
print(1 in NumRomanos)
