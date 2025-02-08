def max_sum_cal(ent_list):

    num = []
    for i in ent_list:
        num.append(int(i))

    max_mul = 0
    
    for i in range(0, 988):
        multify = 1
        
        
        for j in range(13):
            multify *= num[i+j]

        if multify > max_mul:
            max_mul = multify
    print(max_mul)


numbers = list(input())

max_sum_cal(numbers)


