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
    print("Can You Guess the Team?")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please Guess a Letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print("Sorry", guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Congratulatons", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess. Please Choose Letters Only")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations! You Guessed The Word Correctly!")
    else:
        print("Sorry. The Word Was " + word + ". Better Luck Next Time!")


def display_hangman(tries):
    stages = [  # FINAL DIAGRAM AFTER ALL GUESSES ARE INCORRECT
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # hDIAGRAM AFTER FIVE INCORRECT GUESSES
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # DIAGRAM AFTER FOUR INCORRECT GUESSES
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # DIAGRAM AFTER THREE INCORRECT GUESSES
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # DIAGRAM AFTER TWO INCORRECT GUESSES
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # DIAGRAM AFTER ONE INCORRECT GUESS
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # INITIAL HANGMAN DIAGRAM
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
