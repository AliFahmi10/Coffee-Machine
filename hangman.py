import random


def start():
    print('''\n- Type "play" for play the game.\t    - Type "exit" for quit from game.''')
    print('''- Type "help" for game instructions.\t- Type "about" for view about the game.\n''')
    print("- NB: Don't put spaces or other symbols in menu name.")


def game_instructions():
    print("\n", "-" * 60)
    print("""\t>>> About H A N G M A N""")
    print("""
       Hangman is a quick and easy game for at least two 
    people. One player, the "host," makes up a secret 
    word, while the other player tries to guess the word 
    by asking what letters it contains. However, every wrong 
    guess brings them one step closer to losing. In this
    computer game, the computer was the "host".\n""")
    print("\t>>> Instructions to play")
    print("""
    1. The computer will select a word for you to solve.
    2. There will show blank line for each letter of the word.
    3. Start guessing letters.
    4. Guess and type a letter.
    5. If the guess was correct it fills it into the blank 
       where it occurs.
    6. If your guess was wrong, you will lose one try.
    7. There are total of 8 tries.
    8. When your all attempts lose, "You are hanged".
    9. Otherwise you guess the word, "You survived".
    \n Let's play and survive""")
    print("-" * 60)


def about():
    print("\n", "-" * 13, "H A N G M A N", "-" * 13)
    print("""\t\t\t- Version 2020.2.0 -\n
         An famous guessing game\n  Copyright © 2020 AFC Multi-International""")
    print("", "-" * 41)


def game_module():

    word_set = ('asia', 'africa', 'europe', 'australia', 'south-america', 'north-america', 'antarctica')
    selected_word = str(random.choice(word_set))
    hint = list('-' * len(selected_word))
    typed_letter = []
    tries = 8

    while "".join(hint) != selected_word:
        if tries == 0:
            print("\nYou are hanged!\n")
            break
        print()
        print("".join(hint))
        guess = str(input("Input a letter :"))
        if len(guess) != 1:
            print("You should input a single letter")
        elif not guess.islower():
            print("It is not an ASCII lowercase letter")
        elif (guess in typed_letter) or (guess in hint):
            print("You already typed this letter")
        elif guess not in selected_word:
            print("No such letter in the word")
            typed_letter.append(guess)
            tries -= 1
        else:
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    hint[i] = guess
    else:
        print()
        print(selected_word)
        print(f"You guessed the word {selected_word}!")
        print("You survived!\n")


print("\n", "-" * 28, "H A N G M A N", "-" * 28)
print("\t\t\t\t\t\t   - Continents tour -")
start()
menu = input("\nEnter a menu :")

while menu != 'exit':
    if menu == 'play':
        print("_" * 70)
        game_module()
        print("_" * 70, "\n")
        menu = input("\nEnter a menu :")
    elif menu == 'help':
        game_instructions()
        menu = input("\nEnter a menu :")
    elif menu == 'about':
        about()
        menu = input("\nEnter a menu :")
    else:
        print("\nPlease enter a valid menu !!!!!")
        menu = input("\nEnter a menu :")
else:
    print("\n", "-" * 16)
    print("Thanks for playing")
    print("", "-" * 16)
