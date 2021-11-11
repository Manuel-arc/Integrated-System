def count_string(s):
    dic = {}
    lst = []
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    valor = max(dic.values())

    for i in dic:
        if dic[i] == valor:
            lst.append(i)

    if len(lst) == 1:
        print('No repetitions')
        print(lst[0])
    else:
        print(sorted(lst))

string = "Amanhaa de manha vamos almocar sempre"

string_no_repeat = "amewquytghvb"

count_string(string)

