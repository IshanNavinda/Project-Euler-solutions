def prime_check(p):
    if p<2:
        return False
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
        
    return True

def get_prime_number_list(n):
    mylist=[]

    for i in range(3,n,2):
        if prime_check(i):
            mylist.append(i)

    return mylist

def concanate_and_check_prime(num1,num2):
    if prime_check(int(str(num1)+str(num2))) and prime_check(int(str(num2)+str(num1))):
        return True
    
    return False

def list_concanate_check(mylist):
    for i in range(len(mylist)):
        for j in range(i,len(mylist)):
            if not concanate_and_check_prime(mylist[i],mylist[j]):
                return False
        
    return True
    

def myfuction():

    prime_number_list=get_prime_number_list(20000)
    lenth=len(prime_number_list)
    for i in range(lenth):
        
        for j in range(i,lenth):
            if concanate_and_check_prime(prime_number_list[i],prime_number_list[j]):
                
                for k in range(j,lenth):
                    if concanate_and_check_prime(prime_number_list[j],prime_number_list[k]):
                        
                        for l in range(k,lenth):
                            if concanate_and_check_prime(prime_number_list[k],prime_number_list[l]):
                                
                                for m in range(l,lenth):
                                    if concanate_and_check_prime(prime_number_list[l],prime_number_list[m]):
                                        if concanate_and_check_prime(prime_number_list[m],prime_number_list[i]):
                                            mylist1=[prime_number_list[i],prime_number_list[j],prime_number_list[k],prime_number_list[l],prime_number_list[m]]
                                            if list_concanate_check(mylist1):
                                                sumlist=sum(mylist1)
                                                print(sumlist)
                                                return


myfuction()