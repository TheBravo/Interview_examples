import pyautogui as pag
import random as rand



def clickrandomlocation(xl, yt, xr, yb):
    xrand = rand.randrange(xl, xr)
    yrand = rand.randrange(yt, yb)
    pag.moveTo(xrand, yrand)
    pag.sleep(rand.uniform(0.3,0.76))
    pag.leftClick(xrand, yrand)
    pag.sleep(4)

def clickrandomlocation_quick(xl, yt, xr, yb):
    xrand = rand.randrange(xl, xr)
    yrand = rand.randrange(yt, yb)
    pag.moveTo(xrand, yrand)
    pag.sleep(rand.uniform(0.1,0.2))
    pag.leftClick(xrand, yrand)
    pag.sleep(1)

def clickrandomlocation_nc(xl, yt, xr, yb):
    xrand = rand.randrange(xl, xr)
    yrand = rand.randrange(yt, yb)
    pag.moveTo(xrand, yrand)
    pag.sleep(rand.uniform(0.3,0.76))
