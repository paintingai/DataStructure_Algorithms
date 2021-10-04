n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1}-> {t2}-> ', end='')
count = 3
mais = n
total = 0
while mais != 0:
    total = total + mais
    while count <= total:
        t3 = t1 + t2
        print(f'{t3}', end='-> ')
        t1 = t2
        t2 = t3
        count += 1
    print('Fim.')
    mais = int(input('Quantos termos a mais quer mostrar? '))
print(f'O total de {total} termos foram exibidos.')