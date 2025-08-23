import math
from time import time

def count_digits(num):
    count = 0
    while num>0:
        num = num//10
        count += 1
    return count


def count_digits_2(num): # better solution
    count = int(math.log(num,10) + 1)
    return count


def reverse_num(num):
    res = 0
    while num>0:
        last = num%10
        num = num//10
        res = (res*10) + last
    return res


def check_palindrome(num):
    dup = num
    reverse = reverse_num(dup)
    return (reverse == dup)


def check_armstrong(num):
    s = str(num)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if num == sum:
        return True

print(reverse_num(475848))
print(check_palindrome(7867))
print(check_armstrong(371))