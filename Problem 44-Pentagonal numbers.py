#-------------------------------------------------------------------------------
"""T.G.I.NAVINDA"""
#-------------------------------------------------------------------------------

def pentonagal_check(p):
    y=(((24*p)+1)**0.5+1)/6 #search on wikipedia(if y is intiger then p is pentongal......)


    if y==int(y) :
        return True

    else:
        return False
    
def nth_pentagonal_num(n):
    y=n*(3*n-1)/2
    return y

def last_step():
    for i in range(1,5000):
        for j in range(i,5000):
            x=nth_pentagonal_num(i)
            y=nth_pentagonal_num(j)
            if pentonagal_check(x+y) and pentonagal_check(y-x):
                return y-x
                

print(last_step())
        

    
        
        
    
    
