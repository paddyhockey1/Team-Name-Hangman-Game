# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

from teams import team_list

def get_word():
    word = random.choice(team_list)
    return word.upper()

    def play(word):
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Can You Guess the Team Name?")
        print(display_hangman(tries))
        print("\n")
        while not guessed and tries > 0:
            guess = input("Please choose a Letter: ").upper()
            if len guess == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("Sorry. Try Again", guess)
                    elif guess not in word:
                        print(guess "is not in the word.")
                        tries -= 1
                       guessed_letters.append(guess)
                    else:
                        print("Well Done.", guess, "That is correct!")
