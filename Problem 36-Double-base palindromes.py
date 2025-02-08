def palindromic_check(p):
    if str(p)==str(p)[::-1]:
        return True
    
    return False
        
sum=0

for i in range(1,1000001):
    temp_num=bin(i)
    binary_num=int(temp_num[2:])
    if palindromic_check(i):
        if palindromic_check(binary_num):
            sum+=i

print(sum)