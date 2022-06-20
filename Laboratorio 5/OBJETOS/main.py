from aplicacion.banco.cliente_bancario import ClienteBancario

#=========================================
# try: intentar (correr las instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir a string
#-------------------------------------------


#=========================================
# Error por sacar más dinero del que tiene
#-----------------------------------------
try: 
    cliente = ClienteBancario("Jaime Andrade", "Hernández Sánchez", 28, 0.0)
    cleinte.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retiraDInero(400)
    print (cliente.imprimirInfo())

#====================================
# Exception es el objeto más general del error
#--------------------------------------------
except Exception as e:
    print("Error: " + str(e))

#=======================================
#Error por usar un atributo privado
#---------------------------------------
try:
    print(cliente.__nombres)
except Exception as ex:
    print("Error: " +str(ex))

#===================
# FOrma correcta
#--------------------
print (cliente.nombres)
