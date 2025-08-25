# Print all divisors of a number, return the list of them
# 36 : 1,2,3,4,6,9,12,18,36

import math
def AllDivisors(num):
    res = set()
    for i in range(1,int(math.sqrt(num))+1):
        if num%i == 0:
            j = num//i
            res.add(i)
            res.add(j)
    return res

def countDivisors(num):
    count = 0
    for i in range(1,int(math.sqrt(num))+1):
        if num%i == 0:
            if num//i != i:
                count += 2
            else:
                count += 1
    return count

num = 7200
print(AllDivisors(num))
print(countDivisors(num))
print(countDivisors(num)== len(AllDivisors(num)))