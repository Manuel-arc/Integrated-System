def dash_mine(camp):
    for i in range(len(camp)):
        for j in range(len(camp[i])):
            a = 0
            if camp[i][j] == '-':
                if i == 0:
                    if j == 0:
                        if camp[i+1][j] == '#':
                            a += 1
                        if camp[i][j+1] == '#':
                            a += 1
                        if camp[i+1][j+1] == '#':
                            a += 1

                        camp[i][j] = a
                    elif j < len(camp[i])-1:
                        if camp[i+1][j] == '#':
                            a += 1
                        if camp[i][j+1] == '#':
                            a += 1
                        if camp[i+1][j+1] == '#':
                            a += 1
                        if camp[i][j-1] == '#':
                            a += 1
                        if camp[i-1][j-1] == '#':
                            a += 1

                        camp[i][j] = a
                    else:
                        if camp[i+1][j] == '#':
                            a += 1
                        if camp[i-1][j] == '#':
                            a += 1
                        if camp[i-1][j-1] == '#':
                            a += 1

                        camp[i][j] = a

    print(camp)

dash_mine([['-', '#', '-', '-'],
           ['#', '-', '-', '#'],
           ['-', '-', '#', '-'],
           ['-', '-', '-', '#']
          ])

