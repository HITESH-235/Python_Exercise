# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return (-1)
# LEETCODE link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

def brute_force(nums): # O(n^2)
    num = -1
    for x in nums:
        if (x > num) and (-x in nums):
            num = x
    return num


def hash_set(nums):
    seen = set(nums)
    res = 0
    for num in nums:
        if -num in seen:
            res = max(res, abs(num))
        seen.add(num)
    return res

from time import time
import random
lst = [random.randint(-10000, 10000) for _ in range(10000)]

start = time()
print(brute_force(lst))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(hash_set(lst))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")