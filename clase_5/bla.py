import math
def calculadora(x,y,operacion):

    suma = lambda a,b : a+b
    resta = lambda a,b: a-b

    def raiz(a,b):
        return math.sqrt(a)

    funciones = {'suma': suma,
                 'resta': resta,
                 'raiz': raiz}

    return funciones[operacion](x,y)


# voy a suma 2  + 5 = 7
resultado = calculadora(2,5 ,'suma')
print(resultado)

# voy a restar 5  -1 = 4
resultado = calculadora(5,1 ,'resta')
print(resultado)

# voy a restar 16
resultado = calculadora(16,0,'raiz')
print(resultado)
