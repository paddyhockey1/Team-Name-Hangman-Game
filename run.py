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
                        guessed_letters.appedn(guess)
                        word_as_list = 
                        list(word_completion)
                        indices = [i for i. letter in enumerate(word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                            word_completion = "".join(word_as_list)
                        if "-" not in word_completion:
                            guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("Please Guess Again", guess)
                    elif guess != word:
                        print(guess, "Incorrect.")
                        tries -= 1
                        guessed_words.appedn(guess)
            else:
                guessed = True
                word_completion = word
            else:
                print("Sorry, Not a Valid Guess.")
                print(display.hangman(tries))
                print(word_completion)
                print("\n")
            else: 
                print("Well Done! You Are correct")
            else:
                print("Sorry. The Team Was " + word + ". Better Luck Next
                
def display_hangman(tries):

    stages = [
        #FINAL HANGMAN FOR END OF GAME
                """
                     --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
    """,
    #DIAGRAM FOR FIVE INCORRECT GUESSES
    """
     
                    --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
    

    ]
