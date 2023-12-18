import random
import class_prog


# d = class_prog.Dot(1,2)

# print(d)

# f = class_prog.Board(Bor=list(d))

if __name__ == "__main__":

    dot = class_prog.Board().Bor3()

    print(dot[4][2].__dir__())
    print(dot[1][1].set_chip(True))
    print(dot[1][1].chip)

