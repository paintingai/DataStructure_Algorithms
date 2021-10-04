a1 = float(input('Insira o comprimento do primeiro segmento: '))
a2 = float(input('Insira o valor do segundo segmento: '))
a3 = float(input('Insira o valor do terceiro segmento: '))
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Com esses segmentos é possível formar um triângulo', end='')
    if a1 == a2 == a3:
        print('equilátero.')
    elif a1 != a2 != a3 != a1:
        print('escaleno.')
    else:
        print('isósceles.')
else:
    print('Os segmentos informados não podem formar um triângulo.')