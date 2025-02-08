def sum_of_all(n):
    sum1=0
    for i in range(0,n+1):
        sum1+=i**2

    sum2=0
    for i in range(0,n+1):
        sum2+=i

    return (sum2)**2-sum1


print(sum_of_all(100))