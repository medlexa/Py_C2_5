import random
import class_prog

import math

def check_nearby_point(x, y, points, threshold=2):
    for point_x, point_y in points:
        if abs(point_x - x) <= threshold and abs(point_y - y) <= threshold:
            return True  # Если найдена точка рядом, возвращаем True
    return False  # Если ни одна точка не найдена рядом, возвращаем False
# def is_nearby(x1, y1, x2, y2, threshold):
    # distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # return distance <= threshold


def ChekShip(x,y,length,orient,shipPlay):
    # print(f"shipPlay = {shipPlay}")
    li = []
    for a in shipPlay:
        for b in a.get_live():
            li.append(b)

        # if(a.x == x and a.y == y):#если начало совпадает
        #     return False
        # for n in a.get_live():
        #     # print(type(n))
        #     # print(n)
        #     if(n[0] == x and n[1]== y):
        #         return False
    # print(li)
    if check_nearby_point(x,y,li):
        return False
    # for a in li:
        # print(is_nearby(a[0],a[1],x,y,2))
        # if(is_nearby(a[0],a[1],x,y,2)):
            # return False
    return True

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
        else:
            if(x + a < 7):
                rap = False
    
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
        print(a)
        while(True):
            x,y,orient = GetStat(a)
            # print(x,y,orient)
            if(ChekShip(x,y,a,orient,shipPlay)):
                koordM = GetKoord(x,y,orient,a)
                print(f"koordM = {koordM}")

                shipPlay.append(class_prog.Ship(a,x,y,orient,koordM))
                # print(shipPlay)
                break
    
    return shipPlay