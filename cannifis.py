# Zoom to 380
# North Facing
from tools import *
import pyautogui as pag


pag.sleep(3)

while True:
    flag = False
    while True:
        if pag.pixelMatchesColor(711,265, (50,106,33)) == True: # Obstacle 1 (tree climb)
            clickrandomlocation(660,258,743,281)
            break
        elif pag.pixelMatchesColor(705,266, (48,105,32)) == True: # Obstacle 1 (failed 8 reset)
            clickrandomlocation(664,255,751,278)
            break
        elif pag.pixelMatchesColor(682,282, (39,94,26)) == True: # Obstacle 1 (failed 5 reset)
            clickrandomlocation(673,274,747,293)
            break
        else:
            pag.sleep(1)
            continue
    while True:
        if pag.pixelMatchesColor(896,170,  (41,88,30)) == True: # Obstacle 2 (building jump)
            clickrandomlocation(872,156,972,255)
            break
        elif pag.pixelMatchesColor(962,201, (205,205,0)) == True: # Obstacle 2 (stuck on tree)
            clickrandomlocation(910,31,1017,84)
            break
        else:
            pag.sleep(1)
            continue
    while True:
        if pag.pixelMatchesColor(657,509, (42,96,38)) == True: # Obstacle 3 (building jump)
            clickrandomlocation(631,477,685,565)
            break
        else:
            pag.sleep(1)
            continue
    while True:
        if pag.pixelMatchesColor(614,792, (62,100,10)) == True: # Obstacle 4 (building jump)
            clickrandomlocation(574,745,630,823)
            break
        else:
            pag.sleep(1)
            continue
    while True:
        if pag.pixelMatchesColor(879,876, (62,100,10)) == True: # Obstacle 5 (building jump)
            clickrandomlocation(861,861,910,961)
            break
        elif pag.pixelMatchesColor(1129,445, (130,110,78)) == True: # Obstacle 5 (fail right square)
            pag.sleep(4)
            clickrandomlocation(1642,928,1677,959)
            pag.sleep(5)
            clickrandomlocation(1632,843,1656,857)
            pag.sleep(5)
            flag = True
            break
        elif pag.pixelMatchesColor(499,902, (40,16,15)) == True: # Obstacle 5 (fail right square alt)
            pag.sleep(4)
            clickrandomlocation(1642,928,1677,959)
            pag.sleep(5)
            clickrandomlocation(1632,843,1656,857)
            pag.sleep(5)
            flag = True
            break
        elif pag.pixelMatchesColor(561,679, (109,100,100)) == True: # Obstacle 5 (fail left square)
            pag.sleep(4)
            clickrandomlocation(1688,924,1723,957)
            pag.sleep(5)
            clickrandomlocation(1632,843,1656,857)
            pag.sleep(5)
            flag = True
            break
        else:
            pag.sleep(1)
            continue
    if flag == True:
        continue
    while True:
        if pag.pixelMatchesColor(1047,675, (22,73,18)) == True: # Obstacle 6 (building jump)
            clickrandomlocation(1017,654,1072,708)
            break
        else:
            pag.sleep(1)
            continue
    while True:
        if pag.pixelMatchesColor(1726,487, (41,98,22)) == True: # Obstacle 7 (building jump with second possible)
            clickrandomlocation(1669,489,1732,584)
            break
        elif pag.pixelMatchesColor(986,1004, (29,80,55)) == True: # Obstacle 7 (left of normal)
            pag.sleep(2)
            clickrandomlocation(1748,491,1809,575)
            break
        else:
            pag.sleep(1)
            continue
    while True:
        if pag.pixelMatchesColor(937,133, (9,70,16)) == True: # Obstacle 8 (building jump to ground)
            pag.sleep(1)
            clickrandomlocation(919,128,964,175)
            break
        elif pag.pixelMatchesColor(917,544, (205,205,0)) == True: # Obstacle 8 (failed)
            pag.sleep(2)
            clickrandomlocation(1117,126,1145,139)
            pag.sleep(5)
            break
        else:
            pag.sleep(1)
            continue

            