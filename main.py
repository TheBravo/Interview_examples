import pyautogui as pag
import time
import random
from pyclick import HumanClicker
import cv2
# import pygetwindow as pgw

hc = HumanClicker()
move_coordinates = {}
move_region = {}

region_1 = 'region_1.png'
move_1 = 'move_1.png'
region_2 = 'region_2.png'
move_2 = 'move_2.png'
region_3 = 'region_3.png'
move_3 = 'move_3.png'
region_4 = 'region_4.png'
move_4 = 'move_4.png'
region_5 = 'region_5.png'
move_5 = 'move_5.png'
region_6 = 'region_6.png'
move_6 = 'move_6.png'
region_7 = 'region_7.png'
move_7 = 'move_7.png'
region_8 = 'region_8.png'
move_8 = 'move_8.png'
region_9 = 'region_9.png'
move_9 = 'move_9.png'
region_10 = 'region_10.png'
move_10 = 'move_10.png'
region_11 = 'region_11.png'
move_11 = 'move_11.png'
region_12 = 'region_12.png'
move_12 = 'move_12.png'
region_13 = 'region_13.png'
move_13 = 'move_13.png'
region_14 = 'region_14.png'
move_14 = 'move_14.png'
region_15 = 'region_15.png'
move_15 = 'move_15.png'

'''
def maximize_runelite(window_title='Runelite'):
    p = pgw.getWindowsWithTitle(window_title)[0]
    p.minimize()
    p.maximize()


def minimize_runelite(window_title='Runelite'):
    p = pgw.getWindowsWithTitle(window_title)[0]
    p.minimize() 
'''


def move_action(move, c_n, t_1, t_2):
    move_coordinates = list(pag.locateOnScreen(move, confidence=c_n))
    xi = move_coordinates[0]
    yi = move_coordinates[1]
    xw = move_coordinates[0] + move_coordinates[2]
    yh = move_coordinates[1] + move_coordinates[3]
    x = random.randint(xi, xw)
    y = random.randint(yi, yh)
    pag.keyDown('shift')
    hc.move((x,y),(random.uniform(0.4, 0.9)))
    hc.click()     
    pag.keyUp('shift')   
    pag.sleep(random.uniform(0.3, 0.5))
    time.sleep(random.uniform(t_1, t_2))

def move_action_nm(move, c_n, t_1, t_2):
    move_coordinates = list(pag.locateOnScreen(move, confidence=c_n))
    xi = move_coordinates[0]
    yi = move_coordinates[1]
    xw = move_coordinates[0] + move_coordinates[2]
    yh = move_coordinates[1] + move_coordinates[3]
    x = random.randint(xi, xw)
    y = random.randint(yi, yh)
    pag.click(x,y)       
    time.sleep(random.uniform(t_1, t_2))

def move_action_nm_test(move, c_n, t_1, t_2, region=(1691,782,1869,1031)):
    for pos in pag.locateAllOnScreen(move, confidence=c_n):
        xi = (pos[0])
        yi = (pos[1])
        xw = (pos[0] + pos[2])
        yh = (pos[1] + pos[3])
        x = random.randint(xi, xw)
        y = random.randint(yi, yh)
        pag.click(x,y)       
        time.sleep(random.uniform(t_1, t_2))
        
        
    

def move_point(xi, yi, xw, yh, t_1, t_2):
    left = xi
    top = yi
    width = xw
    height = yh
    x = random.randint(left, width)
    y = random.randint(top, height)
    hc.move((x,y),(random.uniform(0.24,0.5)))
    real_click()        
    time.sleep(random.uniform(t_1, t_2))


def move_point_lc(xi, yi, xw, yh, t_1, t_2):
    left = xi
    top = yi
    width = xw
    height = yh
    x = random.randint(left, width)
    y = random.randint(top, height)
    hc.move((x,y),(random.uniform(0.41,0.59)))
    pag.sleep(51 / random.randint(83,201))
    pag.click()        
    time.sleep(random.uniform(t_1, t_2))

def move_point_nc(xi, yi, xw, yh, t_1, t_2):
    left = xi
    top = yi
    width = xw
    height = yh
    x = random.randint(left, width)
    y = random.randint(top, height)
    hc.move((x,y),(random.uniform(0.4, 0.9)))        
    time.sleep(random.uniform(t_1, t_2))


def real_click():
        pag.sleep(48 / random.randint(83,201))
        pag.click()
    


def a():
    move_point(3540,647,3567,677,0.3,0.6)
def b():
    move_point(3604,649,3627,675,0.3,0.6)
def c():
    move_point(3672,649,3692,675,0.3,0.6)
def d():
    move_point(3723,644,3761,671,0.3,0.6)
def e():
    move_point(3529,696,3575,727,0.3,0.6)
def f():
    move_point(3596,699,3635,725,0.3,0.6)
def g():
    move_point(3660,700,3702,724,0.3,0.6)
def h():
    move_point(3723,698,3762,724,0.3,0.6)
def i():
    move_point(3533,751,3571,777,0.3,0.6)
def j():
    move_point(3596,753,3631,774,0.3,0.6)
def k():
    move_point(3661,755,3697,776,0.3,0.6)
def l():
    move_point(3722,755,3764,778,0.3,0.6)
def m():
    move_point(3533,806,3572,829,0.3,0.6)
def n():
    move_point(3598,809,3635,830,0.3,0.6)
def o():
    move_point(3660,808,3694,829,0.3,0.6)
def p():
    move_point(3722,808,3762,832,0.3,0.6)
def q():
    move_point(3533,860,3570,885,0.3,0.6)
def r():
    move_point(3597,862,3635,884,0.3,0.6)
def s():
    move_point(3660,862,3701,886,0.3,0.6)
def t():
    move_point(3724,862,3762,884,0.3,0.6)
def u():
    move_point(3532,914,3568,938,0.3,0.6)
def v():
    move_point(3598,914,3632,936,0.3,0.6)
def w():
    move_point(3659,915,3698,938,0.3,0.6)
def x():
    move_point(3723,914,3759,941,0.3,0.6)
def y():
    move_point(3534,968,3574,993,0.3,0.6)
def z():
    move_point(3597,970,3631,993,0.3,0.6)
def aa():
    move_point(3661,971,3698,992,0.3,0.6)
def ab():
    move_point(3722,972,3761,993,0.3,0.6)



def drop_ores():    
   while True:
        pag.keyDown('shift')
        pag.sleep(1)
        selections = ['first', 'second', 'third', 'fourth']
        selection = random.choice(selections)
        if selection == selections[0]:
            pag.sleep(random.uniform(0.8,1.4))
            a(), b(), c(), d(), e(), f(), g(), h(), i(), j(), k(), l(), m(), n(), 
            o(), p(), q(), r(), s(), t(), u(), v(), w(), x(), y(), z(), aa(), ab()
            pag.keyUp('shift')
            break
        elif selection == selections[1]:
            pag.sleep(random.uniform(0.8,1.4))
            a(), b(), c(), d(), h(), g(), f(), e(), i(), j(), k(), l(), p(), o(), 
            n(), m(), q(), r(), s(), t(), x(), w(), v(), u(), y(), z(), aa(), ab()
            pag.keyUp('shift')
            break
        elif selection == selections[2]:
            pag.sleep(random.uniform(0.8,1.4))
            a(), e(), i(), m(), q(), u(), y(), z(), v(), r(), n(), j(), f(), b(), c(),
            g(), k(), o(), s(), w(), aa(), ab(), x(), t(), p(), l(), h(), d()
            pag.keyUp('shift')
            break
        elif selection == selections[3]:
            pag.sleep(random.uniform(0.8,1.4))
            a(), b(), c(), d(), h(), l(), p(), t(), x(), ab(), aa(), z(), y(), u(), 
            q(), m(), i(), e(), f(), g(), k(), o(), s(), w(), v(), r(), n(), j()
            pag.keyUp('shift')
            break







