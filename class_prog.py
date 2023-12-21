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
        self.board = [[Dot(x, y,"-") for x in range(0,7)] for y in range(7)]
        self.chip = function.randomShip(shipL)
        self.battle = [[]]
    @property
    def GetBat(self):
        return self.battle
    def batAdd(self, value):
        h = self.GetBat
        h.append(value)
        self.battle = h
        # self.battle = value
        

    def GetShip(self):
        return self.chip
    def GetBoard(self):
        return self.board
    
    def ChekShip(self,chip):
        for a in self.chip:
            print(a)
    def PrintBoard(self):
        res = "  | 1 | 2 | 3 | 4 | 5 | 6 | 7"
        # for a in range(0,len(self.board)):
        letters = ['a','b','c','d','e','f','g']
        for i, row in enumerate(self.board):
            l = []
            for b in range(0,len(self.board)):
                l.append(self.board[b][i].get_typ)
            res += f"\n{letters[i]} | " + " | ".join(l) + " |"
        print(res)

    def PrintS(self):
        # for a in range(0,len(self.board)):
        #     for b in range(0,len(self.board)):

        for c in self.chip:
            for c2 in c.live:
                # print (c2)
                self.board[c2[0]][c2[1]].typ("T")
                        # if(c2[0] == self.board[b][a].getX and c2[1] == self.board[b][a].getY):
                        #     self.board[b][a].typ("T")
        # res = "  | 1 | 2 | 3 | 4 | 5 | 6 | 7"
        # # for a in range(0,len(self.board)):
        # letters = ['a','b','c','d','e','f','g']
        # for i, row in enumerate(self.board):
        #     l = []
        #     for b in range(0,len(self.board)):
        #         l.append(self.board[b][i].get_typ)
        #     res += f"\n{letters[i]} | " + " | ".join(l) + " |"
        # print(res)
    def StepP(self,a):
        self.board[a[0]][a[1]].typ("X")
    
    def StepMiss(self,a):
        self.board[a[0]][a[1]].typ("T")



            
class Ai(Player):
    def __init__(self,shipL):
        self.board = [[Dot(x, y,"-") for x in range(0,7)] for y in range(7)]
        self.chip = function.randomShip(shipL)
        self.battle = []

    

    def PrintAi(self):
        self.battle.append([1,3])
        
        print(self.battle)
        for a in self.battle:
            print(a)
            for b in self.chip:
                for c in b.live:
                    # print(c)
                    if(a[0] == c[0] and a[1] == c[1]):
                        print("D[jfds]")
                        self.board[c[0]][c[1]].typ("V")
    

        


