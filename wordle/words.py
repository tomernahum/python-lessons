

# VALID_WORDS_LIST = None


from pathlib import Path



#p = Path("./valid_words.txt")
p1 = Path(__file__).with_name('./valid_words.txt') #opens file from correct directory. got from stackoverflow
with p1.open(mode="r") as file:
	# VALID_WORDS_LIST = file.readlines()
	VALID_WORDS_LIST = [line.rstrip('\n') for line in file]
	

POSSIBLE_SOLUTION_WORDS_LIST = VALID_WORDS_LIST
p2 = Path(__file__).with_name('./possible_solution_words.txt') #opens file from correct directory. got from stackoverflow
with p2.open(mode="r") as file:
	POSSIBLE_SOLUTION_WORDS_LIST = [line.rstrip('\n') for line in file]



LETTERS = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
