import random
from game import playGameV1
from game2 import playGameV2

from words import POSSIBLE_SOLUTION_WORDS_LIST, VALID_WORDS_LIST
def main():
    # config questions
    allow_invalid_words = convert_answer_to_bool(input("Allow invalid words? (y/n) "), default=False)
    harder_words_mode = convert_answer_to_bool(input("Harder Words Mode? (y/n) "), default=False)
    spoil_game = convert_answer_to_bool(input("Spoil the game? (y/n) "), default=False)
    print("")

    if harder_words_mode:
        solution_word = random.choice(VALID_WORDS_LIST)
    else:
        solution_word = random.choice(POSSIBLE_SOLUTION_WORDS_LIST)

    playGameV2(solution_word, VALID_WORDS_LIST, allow_invalid_words=allow_invalid_words, spoil=spoil_game)


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


if __name__ == "__main__":
    main()