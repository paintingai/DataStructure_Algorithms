from random import randint
from time import sleep
lista = list()
jogos = list()
print('=-=' * 20)
print(f"{'JOGO DA MEGA SENA':^60}")
print('=-=' * 20)
qtd = int(input('Quantos jogos quer que sejam sorteados? '))
tot = 1
while tot <= qtd:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('---' * 7, f'SORTEANDO {qtd} JOGOS', '---' * 7)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}.')
    sleep(0.5)
print('Boa Sorte!')