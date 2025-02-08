#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------


from itertools import permutations

def prime_check(p):
    if p < 2:
        return False

    for i in range(2, int(p**0.5)+1):
        if p % i == 0:
            return False

    return True


def maxpandigital():
    maxnum=0
    temp=0

    for i in range(9,1,-1):
        permute=list(permutations(range(1,i+1)))

        for j in permute:
            
            templist=[str(x) for x in j]
            temp=int("".join(templist))

            if prime_check(temp):
                    if temp>maxnum:
                        maxnum=temp
    print(maxnum)

maxpandigital()