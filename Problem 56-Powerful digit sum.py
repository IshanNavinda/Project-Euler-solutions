#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------

def sum_of_each_num(s):
    s=str(s)
    mylist=[int(x) for x in s]

    return sum(mylist)

def myfuction():
    maxsum=0
    for i in range(1,101):
        for j in range(1,101):
            temp=i**j
            temp=sum_of_each_num(temp)

            if temp>maxsum:
                maxsum=temp

    print(maxsum)

myfuction()


