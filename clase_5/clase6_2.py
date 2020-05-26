# python no tiene la switch
# implementar un switch
def f1():
    print('llamando a f1')

def f2():
    print('llamando a f2')

f3 = lambda : print('llamando a lambda')

caja = {'f1_x' : f1,
        'f2_x' : f2,
        'f3_x' : f3}

print('voy a sumar 2 y 4')
calculadora(2,4,'sumar')

caja['f3_x']()
caja['f1_x']()

l = [caja['f1_x'], caja['f2_x'], caja['f3_x']]
l[-1]()

def my_f(a,b):

    a - b -a -a

    return a + b * b

a = my_f(3,4)
l1 = [caja['f1_x'], my_f]
p = l1[-1](3,6)
print(p)

lambda a,b : a +b+a

def raiz(x):
    return math.sqrt(x)

import math
math.pow()
math.sqrt()