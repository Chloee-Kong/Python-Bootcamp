from constant import *

# NumPad is a class of game pad
class NumPad:
    num = NUM
    # pad is a list of chess corresponding to place index 1 to 9, so set 0 as 0
    pad = [0]

    def __init__(self):
        for n in range(1, self.num*self.num + 1):
            self.pad.append(n)

    # show the pad based on the pad list, a record of place and chess
    def display(self):
        turn_count = 0
        pad_s = ''
        for p in self.pad:
            if p == 0:
                continue
            cell = "[" + str(p) + "]"
            pad_s += cell
            turn_count += 1
            if turn_count == self.num:
                pad_s += "\n"
                turn_count = 0

        print(pad_s)
