
# def mi_function(a,b):
#     return a + b

def mi_function(*args):
    return args[::2]
    pass

resultado = mi_function(1,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6)
print(resultado)
pass

# def otra_funcion(parametro1, parametro2):
#     return parametro1 / parametro2
#
# otra_funcion(parametro1=100, parametro2=15)
def mas(*args, **kwargs):
    """

    :param args: esto es para
    :param kwargs: esto otro es para
    :return: resuleve esto
    """
    pass

def otra_funcion(a,b,*args, c, **kwargs):
    # kwargs es un diccionario
    return a + b + args[-1] + mas(*args, **kwargs)

otra_funcion(1,2,3,4,5,c = ['hello', 'bye!'],  parametro1=10,mas=2, parametro2= 3, otros=1000, mas_parametros=8181818181)