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
NO_RECOMMEND = -1

recommendLabel = "recommendLabel.png"
gradeOneLabel = "gradeOneLabel.png"
gradeTwoLabel = "gradeTwoLabel.png"
gradeThreeLabel = "gradeThreeLabel.png"
goodRaceLabel = "goodRaceLabel.png"
recommendRaceRegion = Region(15,623,564,130)
raceRegion = Region(13,622,579,269)
runLabel = "runLabel.png"
backLabel = "backLabel.png"

def checkRaceGrade():
    if not recommendRaceRegion.has(recommendLabel):
        return NO_RECOMMEND

    if recommendRaceRegion.has(gradeOneLabel):
        return GRADE1
    if recommendRaceRegion.has(gradeTwoLabel):
        return GRADE2    
    if recommendRaceRegion.has(gradeThreeLabel):
        return GRADE3


if recommendRaceRegion.has(recommendLabel):
    print(checkRaceGrade())


def runRace(objectiveRace):
    global setEscape

    if not objectiveRace:
        sleep(2)

        check = checkRaceGrade()

        if check == NO_RECOMMEND and not raceRegion.has(goodRaceLabel):
            reg.click(backLabel)
            return False

        if check != GRADE1:
            if raceRegion.has(gradeOneLabel):
                raceRegion.click()
            elif raceRegion.has(goodRaceLabel):
                raceRegion.click()
            else:
                reg.click(backLabel)
                return False

    waitClick(runLabel)
    sleep(2)
    waitClick(runLabel)

    if not setEscape:
        waitClick("1616490307479.png")
        waitClick(Pattern("1621838150892.png").similar(0.80))
        reg.click("1616490367973.png")
        setEscape = True
     
    waitClick("1616365717674.png")

    while not reg.has(Pattern("1616365816547.png").similar(0.60)):
        if reg.has(Pattern("1623291017075.png").similar(0.85)):
            reg.click(Pattern("1623291017075.png").similar(0.85))
            continue 
        
        reg.click(Pattern("1619818624505.png").targetOffset(155,999))
        wait(2)

    
    while reg.has(Pattern("1616365816547.png").similar(0.60)):        
    
        waitClick(Pattern("1616365816547.png").similar(0.60))
        wait(2)
    
    return True


dateRegion = Region(0,63,201,26)

hanshinJFLabel = "hanshinJFLabel.png"

hopefullLabel = "hopefullLabel.png"
victoriaLabel = "victoriaLabel.png"
tennoFallLabel = "tennoFallLabel.png"

dateJunior = Pattern("dateJunior.png").similar(0.90)
dateClassic = Pattern("dateClassic.png").similar(0.90)
dateSinior = Pattern("dateSinior.png").similar(0.90)
dateClassArray = [dateJunior, dateClassic, dateSinior]
CLASS_JUNIOR = 0
CLASS_CLASSIC = 1
CLASS_SENIOR = 2

date1 = Pattern("date1.png").similar(0.90)
date2 = Pattern("date2.png").similar(0.90)
date3 = Pattern("date3.png").similar(0.90)
date4 = Pattern("date4.png").similar(0.90)
date5 = Pattern("date5.png").similar(0.90)
date6 = Pattern("date6.png").similar(0.95)
date7 = Pattern("date7.png").similar(0.90)
date8 = Pattern("date8.png").similar(0.90)
date9 = Pattern("date9.png").similar(0.90)
date10 = Pattern("date10.png").similar(0.90)
date11 = Pattern("date11.png").similar(0.90)
date12 = Pattern("date12.png").similar(0.90)
dateMonthArray = [date12, date11, date10, date9, date8, date7, date6, date5, date4, date3, date2, date1]
MONTH_01 = 11
MONTH_02 = 10
MONTH_03 = 9
MONTH_04 = 8
MONTH_05 = 7
MONTH_06 = 6
MONTH_07 = 5
MONTH_08 = 4
MONTH_09 = 3
MONTH_10 = 2
MONTH_11 = 1
MONTH_12 = 0


dateA = Pattern("dateA.png").similar(0.90)
dateB = Pattern("dateB.png").similar(0.90)
dateWeekArray = [dateA, dateB]
WEEK_FORMER = 0
WEEK_LATER = 1


def checkDateExists(array):
    for index, item in enumerate(array):
        if dateRegion.has(item):
            return index
    return -1

def checkClass():
    return checkDateExists(dateClassArray)

def checkMonth():
    return checkDateExists(dateMonthArray)

def checkWeek():
    return checkDateExists(dateWeekArray)


def checkDate():
    cls = checkClass()
    month = checkMonth()
    week = checkWeek()
    return {'cls': cls, 'month': month, 'week': week}

raceDateArray = [
    #{'cls': CLASS_JUNIOR, 'month': MONTH_12, 'week': WEEK_FORMER}, #阪神JF、朝日杯
    {'cls': CLASS_JUNIOR, 'month': MONTH_12, 'week': WEEK_LATER}, #ホープフル
    {'cls': CLASS_CLASSIC, 'month': MONTH_04, 'week': WEEK_FORMER}, #皐月、桜花賞
    #{'cls': CLASS_CLASSIC, 'month': MONTH_05, 'week': WEEK_FORMER}, #NHK
    {'cls': CLASS_CLASSIC, 'month': MONTH_05, 'week': WEEK_LATER}, #ダービー
    {'cls': CLASS_CLASSIC, 'month': MONTH_11, 'week': WEEK_LATER}, #JC
    {'cls': CLASS_CLASSIC, 'month': MONTH_11, 'week': WEEK_LATER}, #有馬
    {'cls': CLASS_SENIOR, 'month': MONTH_03, 'week': WEEK_LATER}, #大阪杯
    #{'cls': CLASS_SENIOR, 'month': MONTH_04, 'week': WEEK_LATER}, #天皇賞春
    #{'cls': CLASS_SENIOR, 'month': MONTH_05, 'week': WEEK_FORMER}, #ヴィクトリアマイル
    #{'cls': CLASS_SENIOR, 'month': MONTH_06, 'week': WEEK_FORMER}, #安田記念
    #{'cls': CLASS_SENIOR, 'month': MONTH_10, 'week': WEEK_LATER}, #天皇賞秋
    {'cls': CLASS_SENIOR, 'month': MONTH_11, 'week': WEEK_LATER}, #JC
]


def isRaceDay():
    date = checkDate()

    race = next((candidate for candidate in raceDateArray if candidate == date), None)

    print("${0}, ${1}".format(date, race))

    return race != None
