tempsum=2
num=1
my_list=[1]

for _ in range(500):
    for _ in range(4):
        num+=tempsum
        my_list.append(num)

    tempsum+=2

sum=0

for j in my_list:
    sum+=j

print(sum)
