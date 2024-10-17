import random
computer = random.randint(1,6)
you = int(input('Guess the number: '))
is_win = you == computer
print(f'You won: {is_win}, Computer number was {computer}')