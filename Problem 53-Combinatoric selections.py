#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------

def factorial(m):
    temp=1
    for i in range(1,m+1):
        temp*=i

    return temp

def combinatorics(n,r):
    temp=factorial(n)/(factorial(r)*(factorial(n-r)))
    return temp

def last_step():
    count=0
    for n in range(1,101):
        for r in range(1,n+1):
            if combinatorics(n,r)>1000000:
                count+=1

    print(count)

last_step()