newlist = []

for i in range(1, 1000):
    for j in range(1, 1000):
        x = i*j
        if str(x) == str(x)[::-1]:
            newlist.append(i*j)

print(max(newlist))
