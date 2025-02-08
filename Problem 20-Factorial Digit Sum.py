sum=0
mul=1
for i in range(1,101):
    mul*=i

mylis=[x for x in str(mul)]

for i in mylis:
    sum+=int(i)

print(sum)