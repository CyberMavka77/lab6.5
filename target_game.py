"""
Target game module
"""
from typing import List
from string import ascii_uppercase
from random import choice

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = []
    letters = ascii_uppercase
    for _ in range(3):
        row = []
        for _ in range(3):
            letter = choice(letters)
            row.append(letter)
        grid.append(row)
    return(grid)

def get_pure_words(all_words, letters) -> List[str]:
    """
    Gets all words from all_words according to rules.
    """
    pure_words = []
    for word in all_words:
        flag = True
        for letter in word.lower():
            if letter not in letters:
                flag = False
        lower_word = word.lower()
        for letter in letters:
            count = letters.count(letter)
            word_count = lower_word.count(letter)
            if word_count > count:
                flag = False
        if flag and len(word) >= 4 and letters[4] in word:
            pure_words.append(word.lower())
    return list(set(pure_words))

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, 'r') as output_file:
        all_of_it = output_file.read()
    all_words = list(all_of_it.split('\n'))
    return get_pure_words(all_words, letters)

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
    pure_user_words = get_pure_words(user_words, letters)
    for word in pure_user_words:
        if word in words_from_dict:
            pure_user_words.remove(word)
    return pure_user_words

def get_all_missed_words(user_words, dict_words):
    result_words = []
    for item in dict_words:
        if item not in user_words:
            result_words.append(item)
    return result_words

def results():
    """
    Performs game process. Saves results
    """
    grid = generate_grid()
    print(grid)
    letters = []
    for item in grid:
        for char in item:
            letters.append(char.lower())
    dict_word = get_words('en.txt', letters)
    user_words = get_user_words()
    pure_user_entered_words = get_pure_words(user_words, letters)
    number = int(len(pure_user_entered_words))
    missed_words = get_all_missed_words(pure_user_entered_words, dict_word)
    pure_user_words = get_pure_user_words(user_words, letters, dict_word)
    print(number)
    print(dict_word)
    print(missed_words)
    print(pure_user_words)
    with open('results.txt', 'w') as output_file:
        output_file.write(str(number))
        dict_str = "\n"
        for item in dict_word:
            dict_str += (str(item) + " ")
        output_file.write(dict_str)
        missed_str = "\n"
        for item in missed_words:
            missed_str += (str(item) + " ")
        output_file.write(missed_str)
        pure_user_str = "\n"
        for item in pure_user_words:
            pure_user_str += (str(item) + " ")
        output_file.write(pure_user_str)
