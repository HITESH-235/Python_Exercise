def check_Armstrong(num):
    count = 0
    temp = num
    while temp>0:
        temp //= 10
        count += 1
    total = 0
    temp = num
    while temp>0:
        last = temp%10
        temp //= 10
        total += last**count
    return (total == num)

print(check_Armstrong(9474))