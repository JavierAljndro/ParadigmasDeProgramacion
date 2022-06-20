from numba import jit
import numpy
import time

@jit(nopython=True)
def rapido(a):
    t = 0.0
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t

def lento(a):
    t = 0.0
    # Para cada renglón
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t
x = numpy.arange(10000).reshape(100,100)

# La primera llamada incluye el tiempo de compilación 
start = time.time()
rapido(x)
end = time.time()
print("Tiempo incluyendo compilación = %s" %(end-start))

# La segunda llamada es para obtener el tiempo de ejecución 
start = time.time()
rapido(x)
end = time.time()
print("Tiempo de ejecición usando numba = %s" %(end-start))

# Función sin optimizar
start = time.time()
lento(x)
end = time.time()
print("Tiempo de ejecución en python puro= %s" %(end-start))

