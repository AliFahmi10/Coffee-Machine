import random


def greeting():
    player_name = input('Enter your name: ')
    print('Hello,', player_name)
    return player_name


def player_rating(player):
    players = [x.split()[0] for x in open('rating.txt', 'r').readlines()]
    ratings = [i.split()[1] for i in open('rating.txt', 'r')]

    if player not in players:
        rating = 0
        print(player, 0, file=open('rating.txt', 'a'))
    else:
        name_index = players.index(player)
        rating = int(ratings[name_index])
    return rating


def game():
    rating = player_rating(greeting())

    user_choice = input('\n')
    if len(user_choice) == 0:
        choices = ['rock', 'paper', 'scissors']
    else:
        choices = user_choice.split(',')
    print("\nOkay, let's start")

    while user_choice != '!exit':
        user_choice = input()
        computer_choice = random.choice(choices)
        computer_index = choices.index(computer_choice)
        options = choices[computer_index + 1:] + choices[:computer_index]

        if user_choice == '!rating':
            print('Your rating:', rating)
        elif user_choice in choices:
            if user_choice in options[:int(len(options)/2)]:
                print(f'Well done. The computer chose {computer_choice} and failed')
                rating += 100
            elif user_choice == computer_choice:
                print(f'There is a draw ({computer_choice})')
                rating += 50
            else:
                print(f'Sorry, but the computer chose {computer_choice}')
        else:
            print('Invalid input')
    print('Bye!')


game()
