def odd_even(num):
    if num%2==0:
        return "even"
    
    return "odd"

def Collatz_Sequence(p):
    my_list=[p]
    while True:
        if odd_even(p)=="even":
            p=p/2

        elif odd_even(p)=="odd":
            p=3*p+1
        my_list.append(int(p))

        if p==1:
            return len(my_list)

def longest_chain():
    maxlenth=1
    for i in range(1,1000000):
        if Collatz_Sequence(i)>maxlenth:
            mynum=i
            maxlenth=Collatz_Sequence(i)

    print(mynum)

longest_chain()       

            

