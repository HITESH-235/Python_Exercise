def reverse_num(num):
    res = 0
    while num>0:
        last = num%10
        num = num//10
        res = (res*10) + last
    return res

num = 12348574353457347543758347543758347583475437523
print(reverse_num(num))