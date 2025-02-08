def abundant_find(a):
    devisors=[1]
    for i in range(2,int((a**0.5)+1)):
        if a%i==0:
            devisors.append(i)
            devisors.append(int(a/i))
    #if an equal value in list / set can be remove it
    devisors=list(set(devisors))
    
    sum = 0
    
    for j in devisors:
        sum+=j

    if sum>a:
        return True
    
    return False

def sum_of_all_abundant():
    
    abundant_num=[]

    for i in range(11,28124):
        if abundant_find(i):
            abundant_num.append(i)

    sum_of_2=set()

    for j in range(len(abundant_num)):
        for k in range(j,len(abundant_num)):
            temp_sum=abundant_num[j]+abundant_num[k]
            if temp_sum<=28123:
                sum_of_2.add(temp_sum)

    sum=0
    for l in range(28124):
        if l not in sum_of_2:
            sum+=l

    print(sum)



sum_of_all_abundant()