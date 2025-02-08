def prime_find(p):
    if p < 2:
        return False

    for i in range(2, p):
        if p % i == 0:
            return False

    return True


def prime_num(n):
    count = 0
    temp = 2
    while count < n:
        if prime_find(temp):
            count += 1

        temp += 1

    print(temp-1)


x = 10001

prime_num(x)
