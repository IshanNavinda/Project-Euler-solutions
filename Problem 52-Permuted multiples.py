#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------

from itertools import permutations


for i in range (1,1000000):
    numtolist=[]
    for j in str(i):
        numtolist.append(int(j))

    perlist=list(permutations(numtolist))

    #2x cal-----------------------------
    numtolist2=[]
    for k in str(i*2):
        numtolist2.append(int(k))

    numtolist2=tuple(numtolist2)
    #-----------------------------------


    #3x cal-----------------------------
    numtolist3=[]
    for k in str(i*3):
        numtolist3.append(int(k))

    numtolist3=tuple(numtolist3)
    #-----------------------------------


    #4x cal-----------------------------
    numtolist4=[]
    for k in str(i*4):
        numtolist4.append(int(k))

    numtolist4=tuple(numtolist4)
    #-----------------------------------


    #5x cal-----------------------------
    numtolist5=[]
    for k in str(i*5):
        numtolist5.append(int(k))

    numtolist5=tuple(numtolist5)
    #-----------------------------------


    #6x cal-----------------------------
    numtolist6=[]
    for k in str(i*6):
        numtolist6.append(int(k))

    numtolist6=tuple(numtolist6)
    #-----------------------------------


    
    if numtolist2 in perlist and numtolist3 in perlist and numtolist4 in perlist and numtolist5 in perlist and numtolist6 in perlist:
        print(i)
        break