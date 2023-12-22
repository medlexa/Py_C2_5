import random
import class_prog

import math
def create_buffer_from_line(line):
    buffer = []
    for a in line:
        for x in range(a[0] - 1, a[0] + 2):
            for y in range(a[1] - 1, a[1] + 2):
                if(buffer not in [x,y]):
                    buffer.append([x, y])
    n = []
    for i in buffer:
        if i not in n:
            n.append(i)
    n.sort()
    return n

def getmaskoord():
    pass
def check_nearby_point(sh4,mas):
    ch = create_buffer_from_line(sh4)
    # print(f"ch = {ch}")
    # print(f"mas = {mas}")
    for c in ch:
        if(c in mas):
            return True
    
    return False  # Если ни одна точка не найдена рядом, возвращаем False
# def is_nearby(x1, y1, x2, y2, threshold):
    # distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # return distance <= threshold


def ChekShip(koord,shipPlay):
    # print(f"shipPlay = {shipPlay}")
    li = []
    for a in shipPlay:
        for b in a.get_live():
            li.append(b)
    
    if check_nearby_point(koord,li):       
        return False
   
    # print(li)
    # for a in li:
        # print(is_nearby(a[0],a[1],x,y,2))
        # if(is_nearby(a[0],a[1],x,y,2)):
            # return False
    return True
def getRandXY():
    x = random.randint(0,6)
    y = random.randint(0,6)

    return x,y
def GetStat(a):
    rap = True
    #0 горизонтально 1 вертикально
    while(rap):

        x = random.randint(0,6)
        y = random.randint(0,6)
        orient = random.randint(0,1)
        #проверка на выход за границы поля
       
        if(orient == 0):
            if(y + a < 7):
                rap = False
                break
        else:
            if(x + a < 7):
                rap = False
                break
    
    return x,y,orient

def GetKoord(x,y,orient,count):
    listK = []
    if(count > 1):
        listK.append([x,y])
        if(orient == 1):#корабль пойдет вертикально
            for a in range(0,count - 1):
                x = x + 1
                listK.append([x,y])
        else:
            for a in range(0,count - 1):
                y = y + 1
                listK.append([x,y])
    else:#если 1 палуба возвращаем просто координаты
        
        listK.append([x,y])
    
    return listK

#рандомно расставляем корабли
def randomShip(shipL):
    
    shipPlay = []

    for a in shipL:
        # print(a)
        while(True):
            x,y,orient = GetStat(a)
            # print(x,y,orient)
            koordM = GetKoord(x,y,orient,a)
            # print(ChekShip(koordM,shipPlay))
            if(ChekShip(koordM,shipPlay)):

            # if(ChekShip(x,y,a,orient,shipPlay)):
                
            #     print(f"koordM = {koordM}")

                shipPlay.append(class_prog.Ship(a,x,y,orient,koordM,koordM.copy()))
                # print(shipPlay)
                break
    
    return shipPlay