def prime_check(p):
    if p<2:
        return False
    
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
        
    return True

def prime_num():
    mylist=[2]
    for i in range(1,1000000,2):
        if prime_check(i):
            mylist.append(i)

    return mylist

prime_num_list=prime_num()

num=0
maxnum=0
for i in prime_num_list[:78300:-1]:#after some tries i adjust the range 
    n=prime_num_list.index(i)

    for j in range(n):
        sum=0
        count=0
        for k in range(j,n):
            sum+=prime_num_list[k]
            count+=1
            
            if sum>i:
                break #when sum over than i stop the for loop of (k)
            
            if sum == i :
                if count>maxnum:
                    maxnum=count
                    num=i


print(num)
    



