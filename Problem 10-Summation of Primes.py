def prime_fimd(p):
    if p<2 :
        return False
    
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
        
    return True

def sum_cal(s):
    sum=0
    for j in range(2,s):
        if prime_fimd(j):
            sum+=j

    print(sum)

x = int(input())

sum_cal(x)