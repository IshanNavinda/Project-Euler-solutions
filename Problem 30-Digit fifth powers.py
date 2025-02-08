mylist=[]

for i in range(999,1000000):
    tempsum=0
    for j in str(i):
        y=int(j)**5
        tempsum+=y
    
    if tempsum==i:
        mylist.append(i)

sum=0
for i in mylist:
    sum+=i

print(sum)        