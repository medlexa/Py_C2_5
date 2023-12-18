#Класс корабля
class Ship:
    def __init__(self, lenght, x,y,orient,live):
        self.lenght = lenght
        self.x = x
        self.y = y
        self.orient = orient
        self.live = live

    def get_live(self):
        return self.live
    
    def get_orient(self):
        return self.orient

    

class Dot:
    def __init__(self,x,y,chip=False):
        self.x = x
        self.y = y
        self.chip = chip

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    
    @property
    def getX(self):
        return self.x
    
    @property
    def getY(self):
        return self.y
    
    def set_chip(self,ship):
        self.chip = ship
    

    
#класс доски
class Board:
    def __init__(self):
        self.Bor = [[]]

    def Bor3(self):
        self.Bor = [[]]
        for a in range(7):
            c = []
            for b in range(7):
                c.append(Dot(a,b))
            self.Bor.append(c)
        return self.Bor

    
class Player:

    def __init__(self):
        self.board = Dot


