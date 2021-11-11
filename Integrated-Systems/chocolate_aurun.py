def number_choco(money, choco_price):
    choco_buy = money//choco_price

    choco_get = choco_buy//3

    print(f"He can buy {int(choco_buy)} and get {int(choco_get)}")


number_choco(5, 1.2)
