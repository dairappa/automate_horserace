reg = Region(0,0,601,1111)

def waitClick(image, waitSecond = 5):
    reg.wait(image, waitSecond)
    reg.click()


def loop():
    
    if not reg.has("1616053302005.png") and reg.has(Pattern("1615978315697.png").similar(0.85)):
        reg.click()

        if reg.has("1615978551852.png"):
            reg.click("1615978573903.png")
            wait(2)
            # returnせずに次の判定にうつる
        else:
            return True

    
    if reg.has("1615955063604.png"):
       reg.click()


       waitClick("1615955176409.png")

       waitClick("1615955176409.png")
       waitClick("1615955359286.png")
       reg.wait(3)
       reg.click(Pattern("1615955389096.png").targetOffset(-344,250))

       waitClick("1615955437110.png")
       waitClick("1615955468286.png")

       waitClick("1615956221725.png")
       return True

    if has("1615928744521.png"):
        return False
    
    if has(Pattern("1615929011233.png").similar(0.90)):
        click("1615928174362.png")
        wait(1)
        click("1615928199593.png")
        return True



    #if reg.has(Pattern("1615928271653.png").similar(0.90)):
    #    click()
    #    waitClick("1615928199593.png")
    #    return




    if reg.has("1615927881535.png"):
    

        reg.click("1615927881535.png")
        reg.click(Pattern("1615928917678.png").targetOffset(14,-171))
        return True

    # 何にもヒットしなかったのでもう一度ループ
    return True


succeeded = True


while succeeded:
    wait(5)
    succeeded = loop()