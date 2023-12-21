

import random
import class_prog
import function
import re 




def PrintDot(free):
    print("!!!!")
    for i, row in enumerate(range(0,6)):
        k = []
        for a in enumerate(range(0,6)):
            k.append(a)
            
        print(k)
        print(type(k[0]))
        
# d = class_prog.Dot(1,2)

# print(d)

# f = class_prog.Board(Bor=list(d))
def create_buffer_around_point(grid, x, y):
    buffer = []
    for i in range(max(0, x-1), min(len(grid), x+2)):
        row = []
        for j in range(max(0, y-1), min(len(grid[0]), y+2)):
            row.append(grid[i][j])
        buffer.append(row)
    return buffer

def moveD(x,y,player,ap):
    #player который нападает
    #ap которого атакуют
    #должно возвращаться несколько значений 
    # x,y координаты хода
    # по какому полю бьют
    if(len(player.GetBat) > 0):
        if [x,y] not in player.GetBat:
            player.batAdd([x,y])
        else:
            return "match"
    else:
        player.batAdd([x,y])
    #теперь смотрим папал или нет
    po = True
    for a in ap.chip:
        print (a.live)
        if [x,y] in a.live:
            ap.StepP([x,y])
            po = False
            print ("Попадание")
            
            return "next"
            
    
    if(po):
        ap.StepMiss([x,y])

        return "out"
        # for b in a.live:
        #     if()

def getInpCoord(typ,Ai,P):

    if typ == "ai":
        while(True):
            P.PrintBoard()
            #перебор возможных ходов
            x,y = function.getRandXY()
            res = moveD(x,y,Ai,P)
            if(res == "winai"):
                return res
            elif(res == "out"):
                break
            
    else:
        while(True):
            Ai.PrintBoard()
            ih = input("Введите координаты ")
            if(ih == "exit"):
                break

            match = re.search(r'[a-g]',ih)
            match2 = re.search(r'[1-7]',ih)

            if(match is not None and match2 is not None):
                letters = ['a','b','c','d','e','f','g']
                x = int(match2[0]) - 1
                y = letters.index(match[0])

                print (x,y)
                res = moveD(x,y,P,Ai)
                
                if(res == "winpl"):
                    return "winpl"
                elif(res == "match"):
                    print("Вы уже ходили в эту клетку!")
                elif(res == "out"):
                    return res
                    
            else:
                print("Введены не верные координаты!")
            # print (match)
# Пример использования
def Game():
    P = class_prog.Player([3,2,2,1,1,1])
    Ai = class_prog.Ai([3,2,2,1,1,1])

    P.PrintS()
    P.PrintBoard()
    print("-----------------------------------")
    Ai.PrintBoard()
    win = True
    while(win):
        win2 = getInpCoord("user",Ai,P)
        
        if(win2 == "winpl"):
            print("Поздравляем! Вы обыграли компьютер!")
            win = False

        win2 = getInpCoord("ai",Ai,P)
        if(win2 == "winai"):
            print("Выйграл компьютер!")
            win = False
        print (win2)

    return True


if __name__ == "__main__":
    print ("Добро пожаловать в игру Морской бой")
    print("-----------------------------------")
    while(Game()):
        ido = input("Еще партейку? yes no? ")

        if (ido == "no"):
            break

    # P = class_prog.Player([3,2,2,1,1,1])
    # Ai = class_prog.Ai([3,2,2,1,1,1])
    # # print(dir(P.GetShip()[0]))
    # print(P)
    # print(len(P.GetBoard()))
    
    # Ai.PrintS()
    # Ai.PrintAi()
    

    # x,y = function.getRandXY()

    # print(moveD(x,y,Ai))
    # print(Ai.GetBat)
    # x,y = function.getRandXY()
    # print(moveD(x,y,Ai))
    # print(Ai.GetBat)


    # getInpCoord("ai")
    # getInpCoord("user")
    # for a in P.GetShip():
    #     print (a.get_live())
    # P.PrintP()
    # for b in P.PrintP().get_live:
    #     print(b)
    # print(P.GetShip()[1].get_live())
    # print(P.board.getX())
    # print(len(dot[0]))
    # print(dot[4][2].__dir__())
    # print(dot[1][1].set_chip(True))
    # print(dot[1][1].chip)

