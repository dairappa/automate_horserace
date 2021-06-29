sys.path.append("uma_util")
import uma_util

reg = Region(0,0,601,1111)

def waitClick(image, waitSecond = 15):
    reg.wait(image, waitSecond)
    reg.click()

setEscape = False
speedCounter = 24

def runRace():
    global setEscape

    
    waitClick("1616365555818.png")
    wait(2)
    
    waitClick("1616365555818.png")


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



def loop():
    switchApp("umamusume")
    global speedCounter
    if reg.has(Pattern("1623306979891.png").similar(0.95)):
        reg.click()
        return True

    if reg.has("1616475107941.png"):
        reg.click()
        return True

    # not in main menu -> skip
    if not reg.has("1621483478211.png"):
        return True

    if reg.has("1615928744521.png") and reg.has("1616367046236.png"):
        reg.click("1616367046236.png")
        
        waitClick("1615928199593.png")
        return True
        
    if reg.has(Pattern("1616366143315.png").similar(0.75)):
        reg.click()
        if reg.has("1616366183098.png", 5):
            waitClick("1615928199593.png")
            return True
        else:
            # ポップアップが出なかった場合、誤クリックなので流す
            wait(1)

    if speedCounter > 0 and (reg.has(Pattern("1621488859271.png").similar(0.84)) or reg.has(Pattern("1621636995121.png").similar(0.80))):
        speedCounter = 0

    if not speedCounter > 0 and not reg.has(Pattern("1616053302005.png").similar(0.90)) and reg.has(Pattern("1615978315697.png").similar(0.85)) and not reg.has(Pattern("1616368003968.png").similar(0.95)):
        reg.click(Pattern("1615978315697.png").similar(0.85))
        if reg.has("1615978551852.png", 5):
            reg.click("1615978573903.png")
            wait(2)
            # returnせずに次の判定にうつる
        else:
            wait(2)
            if reg.has(Pattern("1616386784155.png").similar(0.95)): 
                reg.click()
                runRace()
                return True
                
            elif reg.has("1616386799656.png") : 
                reg.click()
                runRace()
                return True
            
            elif reg.has(Pattern("1616365555818.png").targetOffset(157,-169)):
                reg.click(Pattern("1616365555818.png").targetOffset(157,-169))
                wait(2)
                if reg.has(Pattern("1616386784155.png").similar(0.90)): 
                    reg.click()
                    runRace()
                    return True
                elif reg.has("1616386799656.png") : 
                    reg.click()
                    runRace()
                    return True
                else:
                   reg.click("1616384941178.png")
                   #　returnせずに次の判定へ
                   wait(3)

            else:
                reg.click("1616384941178.png")
                # returnせずに次の判定へ
                wait(3)




    
    if reg.has("1615955063604.png"):
       reg.click()

       if reg.has("1616387184684.png", 3):
          reg.click("1616387228621.png") 
          wait(3)

       runRace()

       waitClick("1615956221725.png")
       wait(2)
       waitClick("1615956221725.png")
       
       return True

    if reg.has("1616646253345.png"):
       reg.click()
       runRace()

       return True
        
        


    
    if reg.has(Pattern("1615929011233.png").similar(0.90)):
        if reg.has("1615928174362.png") :
            reg.click("1615928174362.png")
            waitClick("1615928199593.png")
            return True
        if reg.has("1616407518547.png"):
            reg.click("1616407518547.png")
            waitClick("1615928199593.png")
            return True



    if reg.has("1615927881535.png"):
    

        reg.click("1615927881535.png")
        reg.click(Pattern("1615928917678.png").targetOffset(14,-171))

        speedCounter = speedCounter - 1
        
        return True



    # 何にもヒットしなかったのでもう一度ループ
    return True


succeeded = True


while succeeded:
    succeeded = loop()
    wait(5)