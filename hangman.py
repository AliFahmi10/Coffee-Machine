import random


def start():
    return input('Type "play" to play the game, "exit" to quit: ')


def game_module():

    word_set = ('python', 'java', 'kotlin', 'javascript')
    selected_word = str(random.choice(word_set))
    hint = list('_' * len(selected_word))
    typed_letter = []
    tries = 8

    while hint != selected_word:
        print()
        print(hint)
        guess = str(input("Input a letter: "))
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
        elif guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    hint[i] = guess
        elif tries == 0:
            print("You are hanged!\n")
            break

    else:
        print()
        print(selected_word)
        print(f"You guessed the word {selected_word}!")
        print("You survived!\n")


print("H A N G M A N")

while start() == 'play':
    game_module()
