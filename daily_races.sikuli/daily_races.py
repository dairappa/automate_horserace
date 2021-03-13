def daily_race():
    wait("1615669377248.png", 10)
    click("1615668587289.png")
    click("1615668605416.png")
    click("1615668625955.png")
    sleep(5)
    click(Pattern("1615668761441.png").targetOffset(250,302))
    click("1615668806865.png")

    hasLimitedSale = has("1615668844266.png", 5)
    if hasLimitedSale:
        click("1615668879912.png")

    
    click("1615668658271.png")

    noTicket = has("1615669525424.png", 5)

    if noTicket:
        click(Pattern("1615669525424.png").targetOffset(-16,-321))
        return False

    return True
    


# main

click("1615496030640.png")

click("1615668399995.png")
click("1615668423272.png")
click("1615668449733.png")
click("1615668465268.png")
sleep(2)
click("1615668936391.png")



succeeded = True

while succeeded:
    suceeded = daily_race()