from numpad import NumPad
from constant import *


def place(place_index, chess_type, pad):
    if place_index in PLACE_RANGE:
        if pad[place_index] in PLACE_RANGE:
            pad[place_index] = chess_type
            return True
        # need to change another place
        else:
            print("There is already a chess, change another place")
            return False
    else:
        print("Please place chess in place 1 - 9")
        return False


# if return true, end the game
def game_end(pad):
    for win in POSSIBLE_WINS:
        if pad[(win[0])] == pad[(win[1])] == pad[(win[2])]:
            print(f'Player with chess {pad[(win[0])]} win!')
            return True
    for p in pad:
        if p in PLACE_RANGE:
            return False
    print("Tie, all places are full")
    return True
