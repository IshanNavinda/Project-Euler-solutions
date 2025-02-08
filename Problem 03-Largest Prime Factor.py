def prime_find(p):
    if p < 2:
        return False

    for i in range(2, p):
        if p % i == 0:
            return False

    return True


def prime_fact(f):
    new = []
    temp = 1
    

    for i in range(2, f):
        if prime_find(i):
            if f % i == 0:
                new.append(i)
                temp *= i

        if temp == f:
            break

    print(new)


prime_fact(600851475143)
