
import random
def rock_paper_scissors():
    print('lets play Rock Paper and Scissors')
    r="rock"
    p="paper"
    s="scissors"
    all_choices=[r,p,s]
    user_input=input(f'Enter ({r},{p},{s}):')
    if user_input not in all_choices:
        print('Invalid input')
        return 
    computer_choice=random.choice(all_choices)
    print(f'user chose {user_input} and computer chose {computer_choice}')
    if computer_choice==user_input:
        print('Tie')
    elif(user_input==r):
        if computer_choice==p:
            print(f'You lose!,{computer_choice} covers {user_input}')
        else:
            print(f'You Win!,{user_input} smashes {computer_choice}')
    elif(user_input==s):
        if computer_choice==p:
            print(f'You Win!,{user_input} cuts{computer_choice}')
        else:
            print(f'You lose!,{computer_choice} smashes {user_input}')
    elif(user_input==p):
        if computer_choice==r:
            print(f'You Win!,{user_input} covers{computer_choice}')
        else:
            print(f'You lose!,{computer_choice} cuts {user_input}')
            