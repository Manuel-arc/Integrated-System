def extract_prime(number):
    number_text = str(number)
    prime_list = []

    for i in range(len(number_text)):
        for j in range(len(number_text)):
            if j+i+1 > 4:
                break
            a = int(number_text[j:j+i+1])
            prime = check_if_prime(a)

            if prime:
                prime_list.append(a)
    prime_list.sort()

    print(prime_list)


def check_if_prime(num):
    flag = True

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
    else:
        flag = False
    return flag









extract_prime(1717)
