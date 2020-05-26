primos = []
for i in range(1,100):
    contador = 0
    for j in primos:
        if (i % j) == 0:
            contador += 1
    if contador < 2 :
        primos.append(i)
pass