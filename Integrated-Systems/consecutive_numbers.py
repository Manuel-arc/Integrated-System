def consecutive_number(numbers):
    numbers_list = numbers.split(",")

    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])

    if all(numbers_list[i] <= numbers_list[i+1] for i in range(len(numbers_list)-1)):
        print("Yes")
    else:
        print('Nao')

    if numbers_list == sorted(numbers_list):
        print('Sim')
    else:
        print('Não')






consecutive_number("1,10,2,3,4,5,6,7,8")
