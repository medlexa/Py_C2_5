#Класс корабля
class Ship:
    def __init__(self, lenght, x,y,orient,live):
        self.lenght = lenght
        self.x = x
        self.y = y
        self.orient = orient
        self.live = live

    
#класс доски
class Dot:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    
class Board:
    def __init__(self):
        self.Bor = []

    
class Player:

    def __init__(self):
        self.board = Dot