import random


def grow_bacteria(final_mass):
    bacteria_mass = [1]
    total_mass = 1
    night = 0

    while total_mass < final_mass:
        num = random.randint(-1, len(bacteria_mass))

        if num != -1:
            for i in range(num):
                bacteria_mass[i] = round(bacteria_mass[i] / 2, 2)
                bacteria_mass.append(bacteria_mass[i])

        for i in range(len(bacteria_mass)):
            bacteria_mass[i] += 1

        total_mass = calculate_mass(bacteria_mass)
        night += 1


    print("It took {} nights".format(night))


def calculate_mass(bac_mass):
    mass = 0

    for i in bac_mass:
        mass += i

    return mass


grow_bacteria(40)
