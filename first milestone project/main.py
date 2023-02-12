from numpad import *
from player import Player
import game

# This is a Tic-Tac-Toe game run main.py and follow the instructions to run

# welcome
print("Welcome to the chess game")
chess_type1 = ''
chess_type2 = ''

# make two players select chess type from X or O
while True:
    chess_type1 = input("Player_1: select your a chess type from X and O:")
    if chess_type1 == "O":
        chess_type2 = 'X'
        print("Player_2: your chess type is X")
        break
    elif chess_type1 == "X":
        chess_type2 = 'O'
        print("Player_2: your chess type is O")
        break
    else:
        print("Please input X or O")

player1 = Player(chess_type1)
player2 = Player(chess_type2)

# create checkerboard
np = NumPad()

# start play
while True:
    np.display()

    # player 1 play and validate the action
    while True:
        place1 = int(input("Player_1: please select a place to play:"))
        if game.place(place1, player1.chess_type, np.pad):
            break

    np.display()

    # check if game end because of tie or one player winner
    if game.game_end(np.pad):
        break

    # player 2 play and validate the action
    while True:
        place2 = int(input("Player_2: please select a place to play:"))
        if game.place(place2, player2.chess_type, np.pad):
            break
    np.display()

    # check if game end
    if game.game_end(np.pad):
        break



