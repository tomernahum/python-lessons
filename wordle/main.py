import random
from words import POSSIBLE_WORDS_LIST
from game import playGameV1
from game2 import playGameV2

def main():
    word = random.choice(POSSIBLE_WORDS_LIST)
    # word = "tomer"
    playGameV2(word, allow_invalid_words=False)

if __name__ == "__main__":
    main()