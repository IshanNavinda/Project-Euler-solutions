#-------------------------------------------------------------------------------
"""-----------------------------T.G.I.NAVINDA--------------------------------"""
"""----------------------------------UOM-------------------------------------"""
#-------------------------------------------------------------------------------


from itertools import permutations

def prime_check(p):
    if p<2:
        return False
    
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
        
    return True

def prime_num_list():
    mylist=[]
    for i in range(1000,4000):
        if prime_check(i):
            mylist.append(i)
        
    mylist.remove(1487) #1487 is already given for us

    return mylist


def permute_check(num1,num2,num3):
    
    mylist1=[x for x in str(num1)]
    mylist1.sort()
    
    mylist2=[x for x in str(num2)]
    mylist2.sort()
    
    mylist3=[x for x in str(num3)]
    mylist3.sort()

    if mylist1==mylist2==mylist3:
        return True
    
    return False

    

prime_numbers=prime_num_list()

def last_step():
    for i in prime_numbers:
        tempnum1=i+3330
        tempnum2=tempnum1+3330

        if prime_check(tempnum1) and prime_check(tempnum2) and permute_check(i,tempnum1,tempnum2):
            print(int(str(i)+str(tempnum1)+str(tempnum2)))
            break

last_step()