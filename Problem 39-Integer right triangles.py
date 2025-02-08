#-------------------------------------------------------------------------------
"""T.G.I.NAVINDA"""
#-------------------------------------------------------------------------------


def myfuncton():
        maxlenth=0
        value=0
        for l in range(1,1001):
            mylist2=[]
            for i in range(1,500):
                for j in range(1,500):
                    y=(i**2+j**2)**0.5

                    mylist1=[]
                    if y+i+j==l:
                        mylist1.append(int(y))
                        mylist1.append(i)
                        mylist1.append(j)
                        mylist1.sort()
                        
                        if mylist1 not in mylist2:
                            mylist2.append(mylist1)
                        
            if len(mylist2)>maxlenth:
                maxlenth=len(mylist2)
                value=l

        print(value)
        print(mylist3)

myfuncton()