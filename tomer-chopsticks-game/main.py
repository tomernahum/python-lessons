
#state.   this could be in a dataclass for easier passing into functions and organization
# right now i just made it global variables. Some people say global vars are bad and you should pass everything to functions explicitly. I'm sure if they are right or not

from utils import ask, ask_boolean, ask_int
from dataclasses import dataclass

@dataclass # optional - adds some default methods for us like __eq__ (is equal to other state classes, called by ==), __repr__ (convert to string, called by str() and print())
class GameState():
    player_1_left_hand:int = 1
    player_1_right_hand:int = 1
    player_2_left_hand:int  = 1
    player_2_right_hand:int = 1

# could make gamestate out of two `class PlayerData()`s
# or could add methods on game state to modify hand based on player
# rn im just using if statements


#TODO getPlayerName class


def main():
    
    # I pass gameState to all the functions, but it could be easier to make gameState a global variable. Technically not doing so makes the functions more reusable for instance if I wanted to have many games at once or something, but thats not realistically going to happen anyway, but suprising things happen + in a more complex project it might happen and people on the internet say global vars are bad apparently...
    # could also make all functions "pure", and make them return gameState instead of modifying it willy nilly

    gameState = GameState(1,1,1,1)

    turn = 1
    winner = None
    while winner == None:
        winner = play_round(gameState, turn)

        if turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1


    pass


def play_round(gameState:GameState, player_turn:int):
    print("------------")

    print(f"Player {player_turn}'s turn")
    printHands(gameState)
    
    if ask_boolean("Do you want to swap hands? "):
        swapHands(gameState, player_turn)
        print("Hands swapped.")
        printHands(gameState)
    
    attackHands(gameState, player_turn)


    return None

def swapHands(gameState:GameState, player:int):

    def isValidMove(move_amount:int):
        #TODO implement
        return True

    num = ask(
        "How many do you want to add from left to right (negative numbers accepted) ", 
        validResponseTypeConverter=int,
        validResponseCheckerFunction=isValidMove
    )

    #todo could be improved upon since repeated, see top of file
    if player == 1: 
        gameState.player_1_left_hand -= num
        gameState.player_1_right_hand += num
    if player == 2: 
        gameState.player_2_left_hand -= num
        gameState.player_2_right_hand += num

def attackHands(gameState:GameState,  player_turn:int): 
    hand_to_attack_with = ask("Which hand do you want to attack with?", validResponses={"left, right"})
    hand_to_attack = ask("Which hand do you want to attack?", validResponses={"left, right"})
    
    if player_turn == 1:
        if hand_to_attack_with = "left"
            if hand_to_attack == "left":
                gameState.player_2_left_hand += gameState.player_1_left_hand


def printHands(gameState:GameState):
    def printHand(numChopsticks):
        for i in range(numChopsticks):
            print("|", end="")
        if numChopsticks == 0:
            print("empty", end="")

    print("Hands:    \tLeft\t\tRight")

    #print player 1 hand
    print(f"Player 1:\t", end="")
    printHand(gameState.player_1_left_hand)
    print("\t\t", end="")
    printHand(gameState.player_1_right_hand)
    print("")

    #print player 2 hand
    print(f"Player 2:\t", end="")
    printHand(gameState.player_2_left_hand)
    print("\t\t", end="")
    printHand(gameState.player_2_right_hand)
    print("")



if __name__ == "__main__":
    main()