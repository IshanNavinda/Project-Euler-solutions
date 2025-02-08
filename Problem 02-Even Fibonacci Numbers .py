first_num = 1
sec_num = 2
total = 0

while first_num <= 4000000:
    if first_num % 2 == 0:
        total += first_num

    first_num, sec_num = sec_num, first_num + sec_num


print(total)
