sys.path.append("training")
sys.path.append("race")
import training
import race


reg = Region(0,0,601,1111)


def waitClick(image, waitSecond = 15):
    reg.wait(image, waitSecond)
    reg.click()


condVeryGood = Pattern("condVeryGood.png").similar(0.80)

classRegion = Region(8,193,149,49)
classDeviewLabel = "classDeviewLabel.png"

raceLabel = "raceLabel.png"
raceKeyLabel = "raceKeyLabel.png"


raceDayLabel = Pattern("raceDayLabel.png").similar(0.90)

mainMenuHeader = "mainMenuHeader.png"

gageHalf = Pattern("gageHalf.png").similar(0.80)

restLabel = "restLabel.png"
okLabel = "okLabel.png"
nextLabel = "nextLabel.png"

trainingLabel = "trainingLabel.png"

notYetLabel = Pattern("notYetLabel.png").similar(0.85)
objectiveRegion = Region(122,85,473,63)
windowTitle = "windowTitle.png"


def loop():
    switchApp("umamusume") 

    if not reg.has(windowTitle):
        return False
    
    if reg.has(Pattern("1623306979891.png").similar(0.95).targetOffset(-226,0)):
        reg.click()
        return True

    if reg.has("1616475107941.png"):
        reg.click()
        return True

    if reg.has(nextLabel):
        reg.click()
        return True

    # not in main menu -> skip
    if not reg.has(mainMenuHeader):
        return True

    if (reg.has("1615928744521.png") or reg.has(Pattern("1626317018337.png").similar(0.85))) and reg.has("1616367046236.png"):
        reg.click("1616367046236.png")
        
        waitClick(okLabel)
        return True
        
    if reg.has("1626393239326.png"):
        reg.click()
        if reg.has("1616366183098.png", 2):
            waitClick(okLabel)
            return True
        else:
            # ポップアップが出なかった場合、誤クリックなので流す
            sleep(1)

    if reg.has(raceDayLabel):
        reg.click(raceDayLabel)
        race.runRace(True)

        try:
            waitClick(nextLabel)
            sleep(2)
            waitClick(nextLabel)
            return True
        except FindFailed:
            print("Final")
            return True

    isRaceDay = race.isRaceDay()

    if (isRaceDay or objectiveRegion.has(notYetLabel)) and not reg.has(raceKeyLabel) and reg.has(raceLabel):
        reg.click(raceLabel)
        if reg.has("1615978551852.png", 5):
            reg.click("1615978573903.png")
            sleep(2)
            # returnせずに次の判定にうつる
        else:
            result = race.runRace(False)

            if result:
                return True
            else:
                # returnせず次の判定にうつる
                sleep(2)
    
    if reg.has(gageHalf):
        if reg.has(restLabel) :
            reg.click(restLabel)
            waitClick(okLabel)
            return True
        if reg.has("1616407518547.png"):
            reg.click("1616407518547.png")
            waitClick(okLabel)
            return True



    if reg.has(trainingLabel):
    

        reg.click(trainingLabel)

        reg.wait("1626318791352.png")

        training.run([1,0.6,1,0.3,0.4])
        
        return True



    # 何にもヒットしなかったのでもう一度ループ
    return True


succeeded = True

while succeeded :
    succeeded = loop()
    wait(2)