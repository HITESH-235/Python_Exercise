# return a list containing all prime factors of a number

import math
def brute_force(num):
    def prime(num):
        if num <= 1:
            return False
        if num%2 == 0:
            return (num == 2)
        for i in range(3,int(math.sqrt(num))+1,2):
            if num%i == 0:
                return False
        return True
    res = []
    for i in range(1,int(math.sqrt(num))):
        if num%i == 0:
            if prime(i):
                res.append(i)
            other = num // i
            if (other) != i and prime(other):
                res.append(num//i)
    return res

def optimised(num):
    res = []
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            res.append(i)
            while num%i == 0:
                num //= i
    if num != 1:
        res.append(num)
    return res

num = 780
print(optimised(num))
print(brute_force(num))