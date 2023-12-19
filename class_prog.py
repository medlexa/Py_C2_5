import function
#Класс корабля
class Ship:
    def __init__(self, lenght, x,y,orient,live):
        self.lenght = lenght
        self.x = x
        self.y = y
        self.orient = orient
        self.live = live#может тут хранить массив координат


    def get_live(self):
        return self.live
    
    def get_orient(self):
        return self.orient

    

class Dot:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type
        # self.chip = chip

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    
    @property
    def getX(self):
        return self.x
    
    @property
    def getY(self):
        return self.y
    
    def set_chip(self,ship):
        print("Установка")
        self.chip = ship
    # @type.setter
    # def type(self,type):
    #     self.type = type
    # @property 
    # def type(self):
    #     print("!")
    #     return self.type
        
    @property
    def get_typ(self):
        """I'm the 'x' property."""
        return self.type

    
    def typ(self, value):
        self.type = value
    

    
#класс доски
class Board:
    def __init__(self):
        self.Bor = [[]]

    # def Bor3(self):
    #     self.Bor = [[]]
    #     for a in range(7):
    #         c = []
    #         for b in range(7):
    #             c.append(Dot(a,b))
    #         self.Bor.append(c)
    #     return self.Bor

    
class Player:

    def __init__(self,shipL):
        self.board = [[Dot(x, y,"-") for x in range(6)] for y in range(6)]
        self.chip = function.randomShip(shipL)

    def GetShip(self):
        return self.chip
    def GetBoard(self):
        return self.board
    
    def ChekShip(self,chip):
        for a in self.chip:
            print(a)

    def PrintP(self):
        for a in range(0,len(self.board)):
            for b in range(0,len(self.board)):

                for c in self.chip:
                    for c2 in c.live:
                        if(c2[0] == self.board[b][a].getX and c2[1] == self.board[b][a].getY):
                            self.board[b][a].typ("T")
        for a in range(0,len(self.board)):
            l = []
            for b in range(0,len(self.board)):
                l.append(self.board[b][a].get_typ)
        print(l)
    


