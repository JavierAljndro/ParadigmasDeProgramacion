##########################
#       Algoritmo 1      #
##########################
#-------------------------------------
# ° Serie exponencial 
# ° Factorización de x
# ° Negativos con una función inversa
#-------------------------------------

n = 200
x = -100.0
flag = False 
if x < 0:
    flag = True
    x = -x
s = 1.0
for i in range(n, 0, -1):
    s *= x/float(i)
    s += 1.0
if flag == True:
    s = 1/s
print(s)
