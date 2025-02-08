def deviors_sum(d):
    #one is divisor ofr all num
    mylist=[1]
    
    for i in range(2,int((d**0.5)+1)):
        if d%i==0:
            mylist.append(i)
            mylist.append(int(d/i))

    mylist=list(set(mylist))


    sum1=0
    for i in mylist:
        sum1+=i
    
    return sum1

def amicable_sum():
    my_list=[]
    for i in range(1,10001):
        x=deviors_sum(i)
        if i == deviors_sum(x) and x!=i :
            my_list.append(i)
            my_list.append(x)
    my_list=list(set(my_list))
    print(my_list)

    sum=0

    for j in my_list:
        sum+=j

    print(sum)
    
    
amicable_sum()