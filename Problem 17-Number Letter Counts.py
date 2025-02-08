from num2words import num2words
sum=0

for i in range(1,1001):
    name=num2words(i)
    name=name.replace(" ","")
    name=name.replace("-","")
    sum+=len(name)
    
    
    
print(sum)
