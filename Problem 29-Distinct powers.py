mylist=[]
for i in range(2,101):
    for j in range(2,101):
        mylist.append(i**j)

mylist=list(set(mylist))

mylist.sort()

print(len(mylist))