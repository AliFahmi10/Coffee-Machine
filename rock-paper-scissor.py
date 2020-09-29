import random

computer = random.choice(['rock', 'paper', 'scissors'])
user = input()

user_lose = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
user_win = {'paper': 'scissors', 'rock': 'paper', 'scissors': 'rock'}

while user != '!exit':
    if user_lose[user] == computer:
        print(f'Sorry, but the computer chose {computer}')
    elif user == computer:
        print(f'There is a draw ({computer})')
    elif (user not in user_lose) or user != '!exit':
        print("Invalid input")
    else:
        print(f'Well done. The computer chose {computer} and failed')
else:
    print('Bye!')
