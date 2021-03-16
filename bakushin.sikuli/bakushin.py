def loop():
　　

    
    if has(Pattern("1615929011233.png").similar(0.90), 5):
        click("1615928174362.png")
        wait(1)
        click("1615928199593.png")
        return True

    if has("1615928744521.png"):
        return False

    #if has(Pattern("1615928271653.png").similar(0.90)):
    #    click("1615928311306.png")
    #    click("1615928199593.png")
    #    return

    if has(Pattern("1615928394745.png").similar(0.90)):
        click(Pattern("1615928394745.png").similar(0.90))
        return True


    if has("1615927881535.png"):
    
        wait("1615927881535.png", 5)
        click("1615927881535.png")
        click(Pattern("1615928917678.png").targetOffset(14,-171))
        return True

    # 何にもヒットしなかったのでもう一度ループ
    return True



succeeded = True
while succeeded:
    succeeded = loop()