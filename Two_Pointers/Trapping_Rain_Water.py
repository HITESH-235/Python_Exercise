# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1. Return the maximum area of water that can be trapped between the bars.
# LEETCODE link: https://leetcode.com/problems/trapping-rain-water/


def trapping_water_Iterative(heights): # --> (int) as units of water trapped
    right_max = 0 # var to store max value from right
    suffic_max = [] # var to store right_max
    n = len(heights)

    for i in range(n-1, -1, -1):
        right_max = max(right_max, heights[i])
        suffic_max.append(right_max)

    suffic_max = suffic_max[::-1]

    left_max = 0
    total = 0

    for i in range(n):
        left_max = max(left_max, heights[i])
        total += min(left_max, suffic_max[i]) - heights[i]
    return total


def trapping_water_TwoPointer(heights):
    n = len(heights)
    left = 0
    right = n - 1
    left_max, right_max = 0, 0
    total = 0

    while left < right:
        left_max = max(left_max, heights[left])
        right_max = max(right_max, heights[right])

        if left_max < right_max:
            total += left_max - heights[left]
            left += 1
        else:
            total += right_max - heights[right]
            right -= 1
    return total


# Example Usage:
heights = []
import random
heights += [random.randint(0, 1000) for _ in range(500)]

from time import time
start = time()
print(trapping_water_Iterative(heights))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(trapping_water_TwoPointer(heights))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")