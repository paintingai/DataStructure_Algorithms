frase = str(input('Insira uma frase: ')).upper().replace(' ', '')
finvertida = frase[::-1]
if frase == finvertida:
    print(f'A frase {frase} é um palíndromo.')
else:
    print(f'A frase {frase} não é um palíndromo.')