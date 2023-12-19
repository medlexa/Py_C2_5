import random
import class_prog
import function





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

if __name__ == "__main__":

    # dot = class_prog.Board().Bor3()
    # print(function.randomShip())

    # free = [class_prog.Dot(x, y,"-") for x in range(6) for y in range(6)]
    # print(free[1])
    # PrintDot(free)
    
    # print(type(free))
    
    P = class_prog.Player([3,2,2,1,1,1])
    # print(dir(P.GetShip()[0]))

    # print(len(P.GetBoard()))
    P.PrintP()
    
    for a in range(0,len(P.GetBoard())):
        # print(a)
        for b in range(0,len(P.GetBoard())):

            for c in P.GetShip():
                for c2 in c.live:
                    # print(f"c = {c2} getX = {P.GetBoard()[b][a].getX } getY = {P.GetBoard()[b][a].getY }")
                    if(c2[0] == P.GetBoard()[b][a].getX and c2[1] == P.GetBoard()[b][a].getY):
                        # print("Попало")
                        P.GetBoard()[b][a].typ("T")
                        # print(P.GetBoard()[b][a].get_typ)
            #print(P.GetBoard()[b][a].getX,P.GetBoard()[b][a].getY)
    
    for a in range(0,len(P.GetBoard())):
        l = []
        for b in range(0,len(P.GetBoard())):
            # print(P.GetBoard()[b][a].get_typ)
            l.append(P.GetBoard()[b][a].get_typ)
        print(l)
            # print(P.GetBoard()[b][a].getY)
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

