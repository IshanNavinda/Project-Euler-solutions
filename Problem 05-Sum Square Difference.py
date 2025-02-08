def devide_check(d):
    for i in range(1, 21):
        if d % i != 0:
            return False

    return True


def funct():
    temp = 21

    while True:
        if devide_check(temp):
            return temp

        temp += 1


print(funct())
