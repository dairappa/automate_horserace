# -*- coding: utf-8 -*-
from sikuli import *

reg = Region(0,0,601,1111)

def waitClick(image, waitSecond = 15):
    reg.wait(image, waitSecond)
    wait(1)
    reg.click()


def team_race():
    sleep(2)

    waitClick(Pattern("1618967182105.png").targetOffset(-12,328))
  
    sleep(2)
    waitClick(Pattern("1618967254003.png").similar(0.60).targetOffset(17,599))


    waitClick("1615496266402.png")

    reg.wait("1615497461594.png",20)

    for i in range(5):

        waitClick("1615496782980.png")

        sleep(1)

        while not (reg.has("1615496782980.png") or reg.has("1619469921064.png")):

            reg.click(Pattern("1615496946031.png").targetOffset(394,396))
            sleep(1)


    while not (reg.has(Pattern("1618967182105.png").targetOffset(14,111)) or reg.has("1615667482724.png")):
        reg.click(Pattern("1615496946031.png").targetOffset(190,999))
        sleep(1)


    if reg.has("1615667482724.png"):
        waitClick(Pattern("1615667573486.png").targetOffset(-107,172))
        waitClick("1616275668460.png")
        waitClick("1616275725222.png")
        
        return False

    return True


# main
def run():
    switchApp("umamusume")
    waitClick("1615496030640.png")
    waitClick("1624254096665.png")
    waitClick(Pattern("1615496097944.png").targetOffset(-12,-136))

    succeeded = True

    while succeeded:
        succeeded = team_race()

    wait(3)

run()