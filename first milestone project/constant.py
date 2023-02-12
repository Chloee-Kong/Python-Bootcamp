# rows of the checkerboard
NUM = 3
# count when create the board
TURN_COUNT = NUM * 3
# cell size of the board
CELL_SIZE = 3
# chess type
CHESS_TYPE = ['X', 'O']
# available place index to place chess
PLACE_RANGE = list(range(1, 10))
# possible wins
POSSIBLE_WINS = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                 [3, 6, 9], [2, 5, 8], [1, 4, 7],
                 [1, 5, 9], [3, 5, 7]]
