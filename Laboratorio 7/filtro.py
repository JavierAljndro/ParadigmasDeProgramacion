##################
# Uso de filtros
##################

#========================================================
# Hacer una lista de los números por arriba del promedio
#========================================================

# Módulo de estadística
import statistics

bigdata = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#=======================================================
# Hazme una lista de elementos que cumplan con la condición 
# x > promedio filter(condición, datos) 
#---------------------------------------------------------
paises = ["", "Argentina", "", "Brasil", "", "Chile", "", "México", "", "Colombia", "", "Cuba", "Venezuela"]

#========================================
# Filtra lo que no contiene nada
#----------------------------------
print(list(filter(None, paises)))
