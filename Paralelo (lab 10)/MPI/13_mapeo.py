from mpi4py import MPI
import math as mate

#////////////////////////////////////////////////////
# "import math as mate" Es un sustituto 
# sirve para que al usar funciones del módulo "math"
# poniendo la instrucción "math.sqrt" pongas el
# el nombre sustituto, en este caso mate
# "mate.sqrt
#////////////////////////////////////////////////////
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 40

x = range(n)
m = int(mate.ceil(float(len(x)) / size))
x_chunk = list(x[rank*m: (rank+1)*m])
r_chunk = list(map(mate.sqrt, x_chunk))

#===================================
# Una sóla lista de todos los datos
#-----------------------------------
r = comm.allreduce(r_chunk)

#==================================
# Una matriz con todos los datos
#----------------------------------
rr = comm.allgather(r_chunk)

#===================================
# Una matriz con todos los datos
#-----------------------------------
rrr = comm.gather(r_chunk, root=1)

if rank == 0:
    print(r)
    print(rr)
    print(rrr)

if rank == 1:
    print(rrr)
