def trianglenum(t):
    num=0
    for i in range(1,t+1):
        num+=i

    return num

def divisors_count(d):
    mylist=[]
    for i in range(1,int((d**0.5)+1)):
        
        if d%i==0:
            mylist.append(i)
            mylist.append(d/i)
            
    return len(mylist)

def final_funct():
    num=0
    while True:
        if divisors_count(trianglenum(num))>=500:
            return num
        num+=1
        
print(trianglenum(final_funct()))

    