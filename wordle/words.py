

VALID_WORDS_LIST = None

with open("./valid_words.txt", 'r') as file:
	# VALID_WORDS_LIST = file.readlines()
	VALID_WORDS_LIST = [line.rstrip('\n') for line in file]
	
POSSIBLE_WORDS_LIST = VALID_WORDS_LIST


LETTERS = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
