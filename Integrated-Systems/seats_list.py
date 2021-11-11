seats = [0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0]

def use_seats(seats):
    a = 0
    s = 0

    for i in range(len(seats)):
        if seats[i] == 0:
            a += 1
        else:
            a = 0

        if a == 5:
            s += 1

    print(s)





use_seats(seats)
