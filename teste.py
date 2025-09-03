'''calculadora'''

numeros = list(range(1,11))

for numero in numeros:
    print(f'\ntabuada do {numero}')
    for other_num in numeros:
        print(f'{numero} * {other_num} = {numero * other_num}')