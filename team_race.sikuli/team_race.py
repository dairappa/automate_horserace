def team_race():
    click(Pattern("1615497174754.png").targetOffset(206,-164))

    sleep(3)

    click("1615497277695.png")

    sleep(2)

    click("1615496266402.png")

    wait("1615497461594.png",10)

    for i in range(5):

        click("1615496782980.png")

        sleep(5)

        click(Pattern("1615496946031.png").targetOffset(394,396))

        sleep(3)


    # TODO: ハイスコア更新対応
    isHighscore = has(Pattern("1615527252775.png").similar(0.50))

    if isHighscore:
        click(Pattern("1615527252775.png").similar(0.50))

    
    wait("1615497350224.png", 10)
    click("1615527387555.png")



    # TODO:　アイテム拾ったとき対応

    hasItem = has(Pattern("1615526489319.png").similar(0.50), 10)

    if hasItem:
        click("1615526540633.png")

    # TODO: 限定セール対応

    limetedSale = has("1615497837455.png", 10)

    if limetedSale:
        click(Pattern("1615497837455.png").targetOffset(-18,-434), 10)
    


    # TODO: ストーリー開放
    newStory = has("1615527447356.png", 10)
    if newStory:
        click("1615527483994.png")


    wait("1615497350224.png", 10)


    click("1615497071387.png")

    sleep(3)

    return True

# main    

click("1615496030640.png")

click("1615496064507.png")
click(Pattern("1615496097944.png").targetOffset(-12,-136))
sleep(3)
click(Pattern("1615497174754.png").targetOffset(206,-164))

sleep(3)

succeeded = True

while succeeded:
    suceeded = team_race()
