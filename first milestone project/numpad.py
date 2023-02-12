from constant import *


# NumPad is a class of game pad
class NumPad:
    num = NUM
    pad = [0]

    def __init__(self):
        for n in range(1, self.num*self.num + 1):
            self.pad.append(n)

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
