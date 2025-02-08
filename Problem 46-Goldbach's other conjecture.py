#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------

import math

def prime_check(p):

    if p<2:
        return False
    
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
        
    return True

def prime_num_list():
    mylist=[]
    for i in range(1,999999,2):
        if prime_check(i):
            mylist.append(i)

    return mylist


def odd_composite_num():
    oddnum=[]
    oddcompositenum=[]
    for i in range(1,100,2):
        oddnum.append(i)

    for j in oddnum:
        for k in oddnum:
            tempnum=int(str(j)+str(k))
            oddcompositenum.append(tempnum)

    oddcompositenum.sort()

    return oddcompositenum

primenumbers=prime_num_list()
oddcompoitenumbers=odd_composite_num()



for k in oddcompoitenumbers:
    condition=True
    for l in primenumbers:
        if l>k:
            break

        tempnum=math.sqrt((k-l)/2)

        if tempnum==int(tempnum):
            condition=False
            break

    if condition:
        print(k)
        break
            

