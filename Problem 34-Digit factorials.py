def fact_sum(num):
    sum=0
    for k in str(num):
        fact=1
        for i in range(1,int(k)+1):
            fact*=i

        sum+=fact

    return sum

allsum=0

for j in range(3,10000000):
    if fact_sum(j)==j:
        allsum+=j

print(allsum)
