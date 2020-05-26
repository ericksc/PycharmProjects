import csv

with open('otro_archivo_csv.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    empleados = [
        ['juan', 'perez', 'medico', 21],
        ['pepe', 'alfaro', 'abogado', 31],
    ]
    for i in empleados:
        writer.writerow(i)