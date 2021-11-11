def buy_lemonade():
    money = 0

    lst = [10, 5, 10, 20]
    payed = True

    for i in lst:
        if i == 5:
            money = 5
        elif i == 10:
            if money < 5:
                payed = False
            else:
                money += 5
        elif i == 20:
            if money < 15:
                payed = False
            else:
                money += 5

    if payed:
        print('Troco correto')
    else:
        print("Nao deu todos")

buy_lemonade()

