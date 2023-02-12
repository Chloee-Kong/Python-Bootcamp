from numpad import *
from player import Player
import game


print("Welcome to the chess game")
chess_type1 = ''
chess_type2 = ''

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

np = NumPad()

# start play
while True:
    np.display()
    while True:
        place1 = int(input("Player_1: please select a place to play:"))
        if game.place(place1, player1.chess_type, np.pad):
            break

    np.display()

    if game.game_end(np.pad):
        break

    while True:
        place2 = int(input("Player_2: please select a place to play:"))
        if game.place(place2, player2.chess_type, np.pad):
            break
    np.display()

    if game.game_end(np.pad):
        break



