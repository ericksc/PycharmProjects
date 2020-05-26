
# ingresos
# gastos

#balance = ingresos - gastos

def gastos(gasolina, netflix, **kwargs):
    return gasolina + netflix


def ingresos(salario, ventas, **kwargs):
    return salario + ventas

def balance(**kwargs):
    return ingresos(**kwargs) - gastos(**kwargs)

datos = {'salario':1000, 'ventas':100, 'gasolina':5, 'netflix':500, 'rifa': 100}

resultado = balance(**datos)