
l = [

    ['pepe',        'naranja',  30],
    ['juancito',    'uva',      29],
    ['andres',      'pera',     29],
    ['carlos',      'manzana',  29],
    ['jose',        'uva',      29],
]

def obtener_columna(n_columna):
    return [i[n_columna] for i in l]

# para obtener el nombre!!
nombres = obtener_columna(0)
print(nombres)

# para obtener la edad!!
edad = obtener_columna(2)
print(edad)

def filtrar_nombre_edad(edad):
    return [
        i[0] for i in l if
            i[2] < edad
    ]

filtro = filtrar_nombre_edad(30)
print(filtro)


pass
