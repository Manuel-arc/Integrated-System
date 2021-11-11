def module(a, b, i=0):

    if b*i == a:
        return 0
    elif b*i < a:
        return module(a, b, i+1)
    else:
        return a-b*(i-1)

print(module(20,6))

