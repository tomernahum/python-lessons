import random
from enum import Enum
from typing import List

import colorama
from colorama import just_fix_windows_console
from colorama import Back
just_fix_windows_console()

from words import POSSIBLE_WORDS_LIST, VALID_WORDS_LIST

class ReadoutValues(Enum):
    exact_match = 1 #"exact_match"
    inexact_match = 2 #"inexact_match"
    no_match = 3 # "no_match"


def playGameV1(solution_word, allow_invalid_words=False):
    for i in range(5):
        guess = getGuess(allow_invalid_words)
        
        #find which letters of guess match
        readout = getReadout(guess, solution_word) #TODO replace strings with enums

        # print(readout)
        prettyPrintReadout(guess, readout)
        
        if guess == solution_word:
            print(f"Congratulations! You won in {i} moves")
            return
    print(f"You lose, the word was {solution_word}")







def getGuess(allow_invalid_words=False):
    while True:
        guess = input("Enter your guess! ").strip().lower()
        if len(guess) != 5:
            print("invalid length, must be 5")
            continue
        if not isRealWord(guess) and not allow_invalid_words:
            print("that word is not in our word bank")
            continue
        break
    return guess;

def isRealWord(word, solution_word=None):
    if word in VALID_WORDS_LIST:
        return True
    if word == solution_word: # not currently made use of in our code
        return True
    return False

def getReadout(guess, solution):
    inexact_match_indexes, exact_match_indexes = getMatches(guess, solution)

    readout:list[ReadoutValues] = []
    for i, letter in enumerate(guess):
        if i in exact_match_indexes:
            readout.append(ReadoutValues.exact_match)
        elif i in inexact_match_indexes:
            readout.append(ReadoutValues.inexact_match)
        else:
            readout.append(ReadoutValues.no_match)

    return readout

def getMatches(guess, solution):
    inexact_match_indexes = []
    exact_match_indexes = []
    for i, letter in enumerate(guess):
        if (letter in solution): #matches
            if guess[i] == solution[i]: #matches exactly
                exact_match_indexes.append(i)
            else: # doesn't match exactly
                inexact_match_indexes.append(i)
    return (inexact_match_indexes, exact_match_indexes)

def uglyPrintReadout(guess, readout:List[ReadoutValues]):
    for i,letter in enumerate(guess):
        if readout[i] == ReadoutValues.exact_match:
            print("exact match:", letter)
        elif readout[i] == ReadoutValues.inexact_match:
            print("inexact match", letter)
        else:
            print("no match", letter)

def prettyPrintReadout(guess, readout:List[ReadoutValues]):
    for i,letter in enumerate(guess):
        prettyPrintLetter(letter, readout[i])

        # if readout[i] == ReadoutValues.exact_match:
        #     print(Back.GREEN + letter, end="")
        # elif readout[i] == ReadoutValues.inexact_match:
        #     print(Back.YELLOW + letter, end="")
        # else:
        #     print(Back.RESET + letter, end="")

    print(Back.RESET)

def prettyPrintLetter(letter, type:ReadoutValues):
    if type == ReadoutValues.exact_match:
        print(Back.GREEN + letter, end="")
    elif type == ReadoutValues.inexact_match:
        print(Back.YELLOW + letter, end="")
    else:
        print(Back.RESET + letter, end="")
    print(Back.RESET, end="") 