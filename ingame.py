# from ui import main as ui
from settings import setsettings
from ahk import AHK
from time import sleep
from clientdetection import clienton
from champselect import champon
from ingamedetection import ingameon
from gamedetection import gameon
import random
from ingame import play

ahk = AHK(executable_path='.\AutoHotkey\AutoHotkey.exe')
clientres = [1024, 576]
resx, resy = None, None
x , y = None, None

def main():
    setsettings()
    # play
    global resx, resy
    # x, y = input("min 1024 768 max 1920 1080\n").split()
    x, y = 1024, 768
    resx = int(x)
    resx = resx - clientres[0]
    resy = int(y)
    resy = resy - clientres[1]
    resy = (resy - 45 )/2 
    client()






def client():
    global resx, resy
    if clienton():
        ahk.click(x=resx+95,y=resy+30) 
        sleep(3)
        ahk.click(x=resx+95,y=resy+30)
        sleep(3)
        ahk.click(x=resx+95,y=resy+30)
        sleep(3)
        ahk.click(x=resx+140,y=resy+80)
        sleep(3)
        ahk.click(x=resx+140,y=resy+80)
        sleep(3)
        ahk.click(x=resx+430,y=resy+550)
        sleep(3)
        ahk.click(x=resx+430,y=resy+550)
        sleep(1)
        ahk.click(x=resx+430,y=resy+550)
        sleep(0.5)
        ahk.click(x=resx+430,y=resy+550)
        while not champon():
            sleep(2)
            ahk.click(x=resx+510,y=resy+445)
        sleep(2)
        ahk.click(x=resx+310, y=resy+130)
        sleep(2)
        ahk.click(x=resx+390, y=resy+130)
        sleep(2)
        ahk.click(x=resx+470, y=resy+130)
        sleep(2)
        ahk.click(x=resx+550, y=resy+130)
        sleep(2)
        ahk.click(x=resx+385,y=resy+85)
        sleep(2)
        ahk.click(x=resx+310, y=resy+130)
        sleep(2)
        ahk.click(x=resx+310, y=resy+130)
        sleep(2)
        ahk.click(x=resx+390, y=resy+130)
        sleep(2)
        ahk.click(512,390)
        ahk.click(x=resx+470, y=resy+130)
        newlist = [[310,135],[390,130],[470,130]]
        rand = random.randint(0,2)
        sleep(2)
        ahk.click(x=newlist[rand][0], y=newlist[rand][1])
        sleep(3)
        ahk.click(x=510,y=540)
        sleep(1)
        ahk.click(x=510,y=550)
        sleep(1)
        ahk.click(x=510,y=560)
        sleep(1)
        sleep(30)
        while not gameon():
            if clienton():
                while not champon():
                    sleep(2)
                    ahk.click(x=resx+510,y=resy+445)
                sleep(2)
                ahk.click(x=resx+310, y=resy+130)
                sleep(2)
                ahk.click(x=resx+390, y=resy+130)
                sleep(2)
                ahk.click(x=resx+470, y=resy+130)
                sleep(2)
                ahk.click(x=resx+550, y=resy+130)
                sleep(2)
                ahk.click(x=resx+385,y=resy+85)
                sleep(2)
                ahk.click(x=resx+310, y=resy+130)
                sleep(2)
                ahk.click(x=resx+310, y=resy+130)
                sleep(2)
                ahk.click(x=resx+390, y=resy+130)
                sleep(2)
                ahk.click(x=resx+470, y=resy+130)
                sleep(1)
                ahk.click(x=510,y=385)
                newlist = [[310+resx,135+resy],[390+resx,130+resy],[470+resx,130+resy]]
                rand = random.randint(0,2)
                sleep(2)
                ahk.click(x=newlist[rand][0], y=newlist[rand][1])
                sleep(3)
                ahk.click(x=510,y=540)
                sleep(1)
                ahk.click(x=510,y=550)
                sleep(1)
                ahk.click(x=510,y=560)
                sleep(1)
                sleep(30)
            gameon()
        # print('gameyes')
        while not ingameon():
            ingameon()
        # print('oye')
        play()
        # print('ez')
        sleep(60)
        ahk.click(x=510,y=615)
        sleep(1)
        ahk.click(x=510,y=615)
        sleep(1)
        ahk.click(x=510,y=615)
        sleep(1)
        ahk.click(x=510,y=380)
        sleep(1)
        ahk.click(x=510,y=380)
        sleep(1)
        ahk.click(x=510,y=615)
        sleep(1)
        ahk.click(x=510,y=615)
        sleep(1)
        ahk.click(x=420,y=630)
        # print('sa')
        sleep(10)
        client()

         
    else:
        sleep(3)
        client()



# def login():
    # name, password, nick = ui()
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.type(name)
    # sleep(0.2)
    # ahk.click(x=resx+, y=resy+)
    # sleep(0.2)
    # ahk.type(password)
    # sleep(0.2)
    # ahk.key_press('Enter')
    # sleep(8)
    # ahk.mouse_position = (1165, 269)
    # ahk.mouse_drag(0, 370, relative=True)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(8)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.type(nick)
    # ahk.click(x=resx+,y=resy+)
    # sleep(0.2)
    # ahk.click(x=resx+,y=resy+)


if __name__ == "__main__":
    main()