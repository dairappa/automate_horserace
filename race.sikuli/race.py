# -*- coding: utf-8 -*-
from sikuli import *

reg = Region(0,0,601,1111)

setEscape = False

def waitClick(image, waitSecond = 15):
    reg.wait(image, waitSecond)
    reg.click()

GRADE1 = 0
GRADE2 = 1
GRADE3 = 2
OTHER = 3

recommendLabel = "recommendLabel.png"
gradeOneLabel = "gradeTwoLabel.png"
gradeTwoLabel = "gradeTwoLabel.png"
gradeThreeLabel = "gradeThreeLabel.png"
recommendRaceRegion = Region(15,623,564,130)
runLabel = "runLabel.png"

def checkRaceGrade():
    if recommendRaceRegion.has(gradeOneLabel):
        return GRADE1
    if recommendRaceRegion.has(gradeTwoLabel):
        return GRADE2    
    if recommendRaceRegion.has(gradeThreeLabel):
        return GRADE3

    return OTHER

if recommendRaceRegion.has(recommendLabel):
    print(checkRaceGrade())


def runRace():
    global setEscape

    waitClick(runLabel)
    wait(2)
    waitClick(runLabel)

    if not setEscape:
        waitClick("1616490307479.png")
        waitClick(Pattern("1621838150892.png").similar(0.80))
        reg.click("1616490367973.png")
        setEscape = True
     
    waitClick("1616365717674.png")

    while not reg.has("1616365816547.png"):
        if reg.has(Pattern("1623291017075.png").similar(0.85)):
            reg.click(Pattern("1623291017075.png").similar(0.85))
            continue 
        
        reg.click(Pattern("1619818624505.png").targetOffset(155,999))
        wait(2)

    
    while reg.has("1616365816547.png"):        
    
        waitClick("1616365816547.png")
        wait(2)