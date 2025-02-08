def myfuc():
    onetonine=[1,2,3,4,5,6,7,8,9]
    pandigitalnumlist=[]
    
    for i in range(100000):
        
        mylist=[]
        temp2=""
        
        for j in range(1,10):
            temp=str(i*j)
            temp2+=temp

            for k in temp:
                mylist.append(int(k))
                mylist.sort()

            if len(mylist)>9:
                break

            if mylist==onetonine:
                pandigitalnumlist.append(int(temp2))
                
    print(max(pandigitalnumlist))

myfuc()