# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas. You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour. Return the minimum integer k such that you can eat all the bananas within h hours.
# Important constraint: piles.length <= h
# LEETCODE link: https://leetcode.com/problems/koko-eating-bananas/description/

from math import ceil
import random
from time import time

def brute_force(piles, h):   # piles - piles, h - max hrs required to eat
    if not piles:
        return False
# rate here is i itself; it goes upto max(piles); because;
# the minimum hours will be obtained if we take rate(i) =  max(piles)
    for i in range(1,max(piles)+1):
        total_hr = 0 # initiating total hr each time we have to loop thr nums
        for num in piles:
            total_hr += ceil(num/i)
        if total_hr <= h:
            return i


def binary_search(piles, h):
    if not piles:
        return False

    def helper(rate):       # rate = bananas per hour
        total_hr = 0
        for i in range(len(piles)):
            total_hr += ceil(piles[i]/rate)
        return total_hr

    left = 1
    right = max(piles)
    res = right             # initialising with max to get min hours

    while left <= right:    # equal sign is for cases where mid = left = right
        mid = left + (right-left)//2
        total_hr = helper(mid)

        if total_hr <= h:   # need smaller rate (more hours hence)
            res = mid # since total hr is within h; curr mid is a probable answer
            right = mid-1   

    # the reason we do not return mid when total hr == h; is because we use ceil;
    # hence there might be a better answer existing as we further minimise mid 
    # if we did not have to use mid, then only "if totalhr == h" would be useful

        else:               # need bigger rate
            left = mid+1
    return res


piles = [random.randint(1,10000) for _ in range(100000)]
h = 1000000
start = time()
print(brute_force(piles, h))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(binary_search(piles, h))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")
