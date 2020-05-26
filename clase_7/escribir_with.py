import time
import datetime

def para_hacer_log(nombre_archivo, info):
    with open(nombre_archivo, 'a+') as f:
        f.write(f'{info}\n')

nombre='mi_log.txt'
c = 0
while True:
    para_hacer_log(nombre_archivo=nombre, info=f'{time.localtime()}')
    print(f'Vamos por {c}')
    time.sleep(1)
    c +=1
    if c > 9:
        break