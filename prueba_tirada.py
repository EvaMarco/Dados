import random
resultado = 0
pooldados = {4: 4, 6: 0, 8: 0, 10: 2, 12: 0, 20: 0}

for i in pooldados:
    value = pooldados.get(i)
    if value != 0:
        for j in range(value):
            number = random.randint(1, i)
            resultado += number
            print(number)

print('El resultado total es', resultado)
