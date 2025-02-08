#-------------------------------------------------------------------------------
"""T.G.I.NAVINDA"""
#-------------------------------------------------------------------------------


def triangle_num():
    mylist1=[]
    for i in range(1,60000):
        n=(i*(i+1))/2
        mylist1.append(int(n))

    return mylist1

def Pentagonal_numbers():
    mylist=[]
    for i in range(1,60000):
        n=i*(3*i-1)/2
        mylist.append(int(n))

    return mylist

def Hexonagal_numbers():
    mylist3=[]
    for i in range(1,60000):
        n=i*(2*i-1)
        mylist3.append(int(n))

    return mylist3

triangle=triangle_num()
Pentagonal=Pentagonal_numbers()
Hexagonal=Hexonagal_numbers()

for k in triangle:
    if k in Hexagonal and k in Pentagonal:
        print(k)


