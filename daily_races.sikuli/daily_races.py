# -*- coding: utf-8 -*-
from sikuli import *

reg = Region(0,0,601,1111)

def waitClick(image, waitSecond = 15):
    reg.wait(image, waitSecond)
    reg.click()


def daily_race():
    waitClick("1615668587289.png")
    waitClick("1615668605416.png")
    waitClick("1615668625955.png")
    sleep(5)
    click(Pattern("1615668761441.png").targetOffset(250,302))
    waitClick("1615668806865.png")

    hasLimitedSale = has("1615668844266.png", 5)
    if hasLimitedSale:
        waitClick("1615668879912.png")

    
    waitClick("1615668658271.png")

    noTicket = has("1615669525424.png", 5)

    if noTicket:
        waitClick(Pattern("1615669525424.png").targetOffset(-16,-321))
        waitClick("1616276117034.png")
        waitClick("1616276140326.png")
        return False

    return True
    


# main
def run():

    waitClick("1615496030640.png")

    waitClick("1617741965676.png")
    waitClick("1615668423272.png")
    waitClick("1615668449733.png")
    waitClick("1615668465268.png")
    waitClick("1615668936391.png")


    succeeded = True

    while succeeded:
        succeeded = daily_race()

    wait(1)

run()