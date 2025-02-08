from itertools import permutations

def permuted_cubes(num):
    num=str(num)
    num_list=[x for x in num]
    num_list=list(permutations(num_list))
    num_list=list(set(num_list))
    count=0

    for temp_list in num_list:

        temp_num=int("".join(temp_list))
        
        if len(str(temp_num))!=len(num):
            continue

        x=round(temp_num**(1/3))
        
        if x**3==temp_num:
            print(temp_num)
            count+=1

    

    if count==5:
        return True
    
    else:
        return False


"""while True:
    cube_num=temp_num**3
    if permuted_cubes(cube_num):
        print(cube_num)
        break
    temp_num+=1"""



        
