# Return True or False if a number is prime or not

import math
def CheckPrime(num):
    if num <= 1:
        return False
    if num%2 == 0:
        return (num == 2)
    for i in range(3,int(math.sqrt(num))+1,2):
        if num%i == 0:
            return False
    return True

num = 997
print(CheckPrime(num))