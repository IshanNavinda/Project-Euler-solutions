# -------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
# -------------------------------------------------------------------------------


def myfuct():
    pandigitlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mylist2 = []
    for i in range(1, 1000):
        for j in range(i, 10000):
            product = i*j
            temp = str(product)+str(i)+str(j)
            if len(temp) != 9:
                continue
            mylist = [int(x) for x in temp]
            mylist.sort()
            if mylist == pandigitlist:
                mylist2.append(product)
    mylist2 = list(set(mylist2))
    print(sum(mylist2))


myfuct()
