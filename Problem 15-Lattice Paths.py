#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------

def myfuction(n):
    mylist=[[0]]
    for i in range(n+1):
        raw=[1]*(i+1)

        if i>0:
            for j in range(1,i):
                raw[j]=mylist[i-1][j-1]+mylist[i-1][j]

            mylist.append(raw)

    tempindex=n

    for k in range(n,0,-1):
        raw=[1]*k

        for l in range(k):
            raw[l]=mylist[tempindex][l]+mylist[tempindex][l+1]
        
        mylist.append(raw)
        tempindex+=1
    

    print(mylist[len(mylist)-1])

myfuction(20)