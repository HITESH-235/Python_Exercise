import math

def count_digits(num):
    count = 0
    while num>0:
        num = num//10
        count += 1
    return count

def count_digits_2(num): # better solution
    count = int(math.log(num,10) + 1)
    return count

num = 832423483274287482342837423742728347237428742747528374823748237428347283576852384723742384725723752384792373285732487585743875834753487534875334754375475
print(count_digits(num))
print(count_digits_2(num))