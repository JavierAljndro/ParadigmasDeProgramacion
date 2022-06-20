from multiprocessing import Process 
import os
import math as M # A la biblioteca "math" la apodo "M"
import time 

def calc():
    for i in range(0, 4000000):
        M.sqrt(i)

procesos = []
cpus = os.cpu_count()
print("Núcleos en tu CPU: ", cpus)
for i in range(cpus):
    print("registrando el hilo %d" %i)
    procesos.append(Process(target=calc))

start = time.time()

for proceso in procesos:
    proceso.start()

for proceso in procesos:
    proceso.join()

end = time.time()
print("se tardó: ", end-start)
