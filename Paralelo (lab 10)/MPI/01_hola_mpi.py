#==============================================
# Para correr el programa es con cualquiera de 
# las siguientes instrucciones:

# " mpiexec -n 4 python3 01_hola_mpi.py"
# " mpirun -n 4 python3 01_hola_mpi.py "
#----------------------------------------------
# En  general :
# mpirun -n [núm. de procesos] python3 [nombre del programa]
#===============================================

from mpi4py import MPI

#============================
# Crear un objeto comunicador
#----------------------------
comunicadores = MPI.COMM_WORLD

#===========================
# Número total de procesos
#---------------------------
n_procesos = comunicadores.Get_size()

#=====================================
# Número identificador de este proceso
#-------------------------------------
quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso", str(quien_soy), "de ", str(n_procesos))
