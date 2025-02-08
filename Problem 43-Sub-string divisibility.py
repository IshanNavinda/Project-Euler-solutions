#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------

from itertools import permutations

perlist=list(permutations(range(10)))
primelist=[2,3,5,7,11,13,17]
mylist=[]

for i in perlist:

    templist=[str(x) for x in i]
    tempnum="".join(templist)
    
    temp=0
    for j in range(1,8):
        
        tempnum2=int(tempnum[j:j+3])
        
        if tempnum2%primelist[j-1]!=0:
            break

        if tempnum2%primelist[j-1]==0:
            temp+=1
            
    if temp==7:
        mylist.append(int(tempnum))

print(sum(mylist))