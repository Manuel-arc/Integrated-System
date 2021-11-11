from random import randint

lst = [4,2,1,10,8]
new_list = []

cont = True
a = 0

while a < len(lst)-1:
    if lst[a] > lst[a+1]:
        lst[a] += lst[a+1]
        lst.remove(lst[a+1])
        a-=1
    a+=1

print(lst) 
