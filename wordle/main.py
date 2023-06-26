import random
from words import POSSIBLE_WORDS_LIST
from game import playGameV1
from game2 import playGameV2

def convert_answer_to_bool(ans:str, default=None):
    ans = ans.strip().lower()
    if ans in {"y", "yes", "1", "t"}:
        return True
    elif ans in {"n", "no", "0", "f"}:
        return False
    else:
        if default == None:
            raise ValueError("Could not convert answer to boolean")
        else:
            return default

def main():
    word = random.choice(POSSIBLE_WORDS_LIST)
    allow_invalid_words = convert_answer_to_bool(input("Allow invalid words? (y/n) "), default=False)
    playGameV2(word, allow_invalid_words, spoil=True)

if __name__ == "__main__":
    main()