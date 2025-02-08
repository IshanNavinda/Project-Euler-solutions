#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------

def palindomic_check(p):
    return str(p)==str(p)[::-1]

def get_palindromic(g):
    return int(str(g)[::-1])

def Lychrel_number_count():
    count=0
    for i in range(1,10001):
        condition=True
        temp=i
        for _ in range(50):
            temp+=get_palindromic(temp)
            if palindomic_check(temp):
                condition=False

        if condition:
            count+=1

    print(count)

Lychrel_number_count()

