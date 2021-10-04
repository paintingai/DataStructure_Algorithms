from random import randint
from time import sleep
computer = randint(0, 10)
print('I thought in a number between 0 and 10. Can you guess?')
sleep(0.5)
player = int(input('What is your guess? '))
count = 0
while computer != player:
    if player < computer:
        print('Try a bigger number...')
        player = int(input('Try again: '))
    elif player > computer:
        print('Try a smaller number...')
        player = int(input('Try again: '))
    count += 1
print(f'Congratulations! You won me with {count} guesses.')