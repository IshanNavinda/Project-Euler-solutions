def prime_check(p):

    if p<2 :
        return False
    
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
        
    return True

def circle_list_and_check(mylist):
    mylist2=[]
    for _ in range(len(mylist)):
        temp=mylist[0]
        for j in range(len(mylist)-1):
            mylist[j]=mylist[j+1]
        
        mylist[len(mylist)-1]=temp

        num=""
        
        for k in mylist:
            k=str(k)
            num+=k

        num=int(num)

        mylist2.append(num)

    return mylist2

def all_prime(mylist):
    for l in circle_list_and_check(mylist):
        if not prime_check(l):
            return False
        
    return True

def last_step():
    allnum=0
    for i in range(1000001):
        my=[]
        i=str(i) 
        for k in i:
            my.append(k)

        if all_prime(my):
            allnum+=1

    print(allnum)

last_step()         
