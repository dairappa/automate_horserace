sys.path.append("util")
import util

setEscape = False

def runRace():
    global setEscape
    
    reg.click("1616365555818.png")
    wait(2)
    
    reg.click("1616365555818.png")

    if not setEscape:
        waitClick("1616490307479.png")
        waitClick(Pattern("1616490330308.png").similar(0.85))
        reg.click("1616490367973.png")
        setEscape = True
     
    waitClick("1616365717674.png")


    while reg.has("1616365717674.png", 3):    
        reg.click()
        wait(1)
    
    wait(3)
    reg.click(Pattern("1615955389096.png").targetOffset(268,627))
    
    waitClick("1616365790564.png")
    waitClick("1616365816547.png")



def loop():
    if reg.has(Pattern("1617103975184.png").similar(0.90)):
        reg.click()
        return True
    
    if not reg.has(Pattern("1616053302005.png").similar(0.90)) and reg.has(Pattern("1615978315697.png").similar(0.85)) and not reg.has(Pattern("1616368003968.png").similar(0.95)):
        reg.click(Pattern("1615978315697.png").similar(0.85))
        if reg.has("1615978551852.png", 5):
            reg.click("1615978573903.png")
            wait(2)
            # returnせずに次の判定にうつる
        else:
            wait(2)
            if reg.has(Pattern("1616386784155.png").similar(0.90)): 
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
       waitClick("1615956221725.png")
       wait(2)
       waitClick("1615956221725.png")
       return True
        
        

    if reg.has("1615928744521.png") and reg.has("1616367046236.png"):
        reg.click("1616367046236.png")
        
        waitClick("1615928199593.png")
        return True
        
    if reg.has(Pattern("1616366143315.png").similar(0.90)):
        reg.click()
        if reg.has("1616366183098.png", 5):
            waitClick("1615928199593.png")
            return True
        else:
            # ポップアップが出なかった場合、誤クリックなので流す
            wait(1)
    
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
        return True

    if reg.has("1616475107941.png"):
        reg.click()
        return True
    

    # 何にもヒットしなかったのでもう一度ループ
    return True


succeeded = True


while succeeded:
    succeeded = loop()
    wait(12)