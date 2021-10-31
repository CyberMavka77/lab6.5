from functools import reduce
from typing import List
import string
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = []
    letters = string.ascii_uppercase
    for _ in range(3):
        row = []
        for _ in range(3):
            letter = random.choice(letters)
            row.append(letter)
            letters = letters.replace(letter, "")
        grid.append(row)
    return(grid)

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, 'r') as output_file:
        all_of_it = output_file.read()
    all_words = list(all_of_it.split('\n'))
    pure_words = []
    for word in all_words:
        flag = True
        for letter in word.lower():
            if letter not in letters:
                flag = False
        if flag and len(word) >= 4:
            pure_words.append(word.lower())
    return list(set(pure_words))

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    end_trigg = True
    while end_trigg:
        try:
            user_words.append(input())
        except EOFError:
            end_trigg = False
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass

print(generate_grid())