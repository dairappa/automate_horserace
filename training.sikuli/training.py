# -*- coding: utf-8 -*-
from sikuli import *

SPEED = 0
STAMINA = 1
POWER = 2
GUTS = 3
SMART = 4

speedClick = Pattern("speedClick.png").targetOffset(9,-128)
staminaClick = Pattern("speedClick.png").targetOffset(114,-128)
powerClick = Pattern("speedClick.png").targetOffset(220,-128)
gutsClick = Pattern("speedClick.png").targetOffset(315,-128)
smartClick = Pattern("speedClick.png").targetOffset(420,-128)

clicks = [speedClick, staminaClick, powerClick, gutsClick, smartClick]

speedIcon = "speedIcon.png"
staminaIcon = "staminaIcon.png"
powerIcon = "powerIcon.png"
gutsIcon = "gutsIcon.png"
smartIcon = "smartIcon.png"

icons = [speedIcon, staminaIcon, powerIcon, gutsIcon, smartIcon]

hintIcon = "hintIcon.png"

determinLabel = Pattern("determinLabel.png").similar(0.50)

friendRegion = Region(485,187,101,500)
determinRegion = Region(35,939,528,89)

def checkFriend():
    iconCountArr = []
    
    for icon in icons:
        iconFound = friendRegion.findAll(icon)
        count = 0
        for iconItem in iconFound:
            count += 1
        iconCountArr.append(count)

    return iconCountArr

def checkTrainingType():
    determinIcon = determinRegion.find(determinLabel)
    determinIconX = determinIcon.getX()
    
    if determinIconX > 480:
        return SMART
    elif determinIconX > 375:
        return GUTS
    elif determinIconX > 270:
        return POWER
    elif determinIconX > 165:
        return STAMINA
    else:
        return SPEED

def run(trainingRate):    
    determinRegion.wait(determinLabel)
    
    iconCountMatrix = []
    
    for index, clickItem in enumerate(clicks):
        if checkTrainingType() != index:
            click(clickItem)
        sleep(1)
        iconCountMatrix.append(checkFriend())
    
    candidates = [sum(iconCountMatrix[i]) * trainingRate[i] for i in range(5)]

                           
    training = candidates.index(max(candidates))
    
    if checkTrainingType() != training:
        click(clicks[training])
        sleep(1)
    
    click(clicks[training])







