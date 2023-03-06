from tools import *
import pyautogui as pag

pag.sleep(5)

while True:
    while True:
        if pag.pixelMatchesColor(22,456, (56,44,9)) == True: # Obstacle 2 (building jump)
            clickrandomlocation_quick(1845,793,1864,805)
            clickrandomlocation_quick(1845,793,1864,805)
            clickrandomlocation_nc(637,56,1607,927)        
            pag.sleep(rand.uniform(22.4,43.1))
            break
        else:
            pag.sleep(1)
            continue
