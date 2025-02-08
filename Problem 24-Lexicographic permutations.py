from itertools import permutations

mylist1 = list(permutations(range(10)))
mylist1.sort()

mylist2=mylist1[999999]

for i in mylist2:
    print(i,end="") 
    



    