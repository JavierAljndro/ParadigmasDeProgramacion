#==========================================
# Uso de reducciones (colapsar resultados)
#==========================================

#=================================================
# Multiplicación de todos los números en la lista
#-------------------------------------------------

from functools import reduce 

bigdata = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#===================
# Función x*y
#------------------
multiplicar = lambda x,y: x*y

print(reduce(multiplicar, bigdata))


#=======================================================
# Reduce le aplica la función por pares a los resultados y 
# el sieguiente elemento comenzando con loss primeros
# elementos.
#=========================================================
