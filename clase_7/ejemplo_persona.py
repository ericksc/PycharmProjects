
with open('estudiantes.txt') as f:
    contenido = f.readlines()

data = [reglon.strip().split(',') for reglon in contenido]
print(data)
pass