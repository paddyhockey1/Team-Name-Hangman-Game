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