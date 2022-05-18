######  e^(2-x)-7x=0  #####

import matplotlib.pyplot as plp
from math import exp

def fn1(x):
    return exp(2-x) - 7*x

def fn2(x):
    return -exp(2-x) -7

x0 = 1.5

x1 = x0 - (fn1(x0) / fn2(x0))

print('2DO PTO:', x1)

#Tercer punto
x2 = x1 -(fn1(x1) / fn2(x1))

print('3ER PTO:', x2)

#Cuarto punto
x3 = x2 - (fn1(x2) / fn2(x2))

print('4TO PTO: ', x3)
print('VALOR ES: ', fn1(x3))
print('RAIZ: ', x3)

x = [-2, -1, 0, 1, 2]
y = [68.59815, 27.085537, 7.38056, -4.281718, -13]

plp.plot(x, y)
plp.show()

y1 = [-61.59815, -27.085537, -14.389056, -9.718282, -8]

plp.plot(x, y1)
plp.show()