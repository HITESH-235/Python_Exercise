# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas. You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour. Return the minimum integer k such that you can eat all the bananas within h hours.
# LEETCODE link: https://leetcode.com/problems/koko-eating-bananas/description/

from math import ceil
import random
from time import time

def brute_force(nums, h):   # nums - piles, h - max hrs required to eat
    if not nums:
        return False

    for i in range(1,max(nums)):
        total_hr = 0
        for num in nums:
            total_hr += ceil(num/i)
        if total_hr <= h:
            return i


def binary_search(nums, h):
    if not nums:
        return False

    def helper(rate):       # rate = bananas per hour
        total_hr = 0
        for i in range(len(nums)):
            total_hr += ceil(nums[i]/rate)
        return total_hr

    left = 1
    right = max(nums)
    res = right             # initialising with max to get min hours

    while left <= right:    # equal sign is for cases where mid = left = right
        mid = left + (right-left)//2
        total_hr = helper(mid)

        if total_hr <= h:   # need smaller rate (more hours hence)
            res = mid
            right = mid-1   
        else:               # need bigger rate
            left = mid+1
    return res


nums = [random.randint(1,10000) for _ in range(100)]
h = 112
start = time()
print(brute_force(nums, h))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(binary_search(nums, h))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")
