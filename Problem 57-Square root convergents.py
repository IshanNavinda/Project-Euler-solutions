#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------


def myfuction():
    denominator_list=[2,5,12,29]
    numerator_list=[3,7,17,41]
    count=0
    for i in range(4,1000):
        denominator=numerator_list[i-1]+denominator_list[i-1]
        numerator=denominator+denominator_list[i-1]
        if len(str(denominator))<len(str(numerator)):
            count+=1

        denominator_list.append(denominator)
        numerator_list.append(numerator)

    print(count)

myfuction()

