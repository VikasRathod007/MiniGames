
import random

def guess_the_number(x):
    print('Lets play Guess The Number')
    random_number=random.randint(0,x)
    num_guesses=0
    while True:
        guess=int(input(f'Guess The Number between 0 and {x}:'))
        num_guesses+=1
        if guess== random_number:
            print(f'congrats, the number is {random_number}')
            break
        elif guess < random_number:
            print('Guess higher number')
        else:
            print('guess lower number')
        
    