from random import randint
import numpy as np

def kill_prisioner(people, step):
    lst = []

    for i in range(people):
        lst.append(i+1)

    print(lst)

    num = randint(0, people-1)

    while people != 1:
        if lst[num] != 0:
            lst[num] = 0

        num += step
        people -= 1

        if num >= len(lst):
            num -= len(lst)

    nonzero = np.nonzero(lst)

    print(lst)
    print(nonzero)








kill_prisioner(5, 2)
