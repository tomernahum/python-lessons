from typing import List

from game import getGuess, getReadout, prettyPrintReadout, getMatches, ReadoutValues, prettyPrintLetter
from words import LETTERS



class Guess:
    def __init__(self, guess_word, solution_word) -> None:
        self.word = guess_word
        self.readout = getReadout(guess_word, solution_word)
    
    def prettyPrintReadout(self):
        prettyPrintReadout(self.word, self.readout)



def playGameV2(solution_word, allow_invalid_words=False):
    past_guesses = []
    letters_knowledge = {}
    for i in range(5):
        guess_word = getGuess(allow_invalid_words)
        
        guess = Guess(guess_word, solution_word)
        updateLettersKnowledge(guess.word, solution_word, letters_knowledge)
        
        past_guesses.append(guess)
        printScreen(past_guesses, letters_knowledge)
        
        if guess.word == solution_word:
            print(f"Congratulations! You won in {i+1} guesses")
            return
        

    print(f"You lose, the word was {solution_word}")

def updateLettersKnowledge(guess_word, solution_word, letters_knowledge:dict):
    inexact_match_indexes, exact_match_indexes = getMatches(guess_word, solution_word)

    for i, letter in enumerate(guess_word):
        if i in exact_match_indexes:
            letters_knowledge[letter] = ReadoutValues.exact_match
        elif i in inexact_match_indexes and letters_knowledge.get(letter) != ReadoutValues.exact_match:
            letters_knowledge[letter] = ReadoutValues.inexact_match
        else:
            letters_knowledge[letter] = ReadoutValues.no_match


def printScreen(guesses:List[Guess], letters_knowledge:dict, overwrite=True):
    if overwrite:
        #TODO Actually Overwrite previous board / clear terminal
        # print("")
        pass

    print("")
    for guess in guesses:
        guess.prettyPrintReadout()
    for i in range(5 - len(guesses)):
        # print("_____")
        print("-----")
    
    print("")
    printKeyboard(letters_knowledge)
    print("")

def printKeyboard(letters_knowledge):
    for letter in LETTERS:
        try:
            prettyPrintLetter(letter.upper(), letters_knowledge[letter])
        except KeyError:
            prettyPrintLetter(letter.upper(), ReadoutValues.no_match)
    print("")

